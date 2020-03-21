import datascraper
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from multiprocessing import Pool
import time

def addToBasket(url_size, driver):
    driver.get(url_size[0])
    #if cookies!=None:
    #    for c in cookies:
    #        driver.add_cookie(c)
    if len(url_size)==2:
        dropdown=Select(driver.find_element_by_xpath('//*[@id="size"]'))
        dropdown.select_by_visible_text(url_size[1].strip())
    driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/form/fieldset[2]/input").click()
    #cookies=driver.get_cookies()
    time.sleep(1)
    #return cookies
def findChoosenItems(jsonObj):
    productsToBuy=[]
    for category in jsonObj:
        for product in jsonObj[category]:
            currentProduct=jsonObj[category][product]
            if currentProduct["BuyIt"]:
                tmp=len(productsToBuy)
                for i in range(len(currentProduct["Colours"])):
                    if currentProduct["Colours"][i][0]=='*':
                        productsToBuy.append([currentProduct["URLs"][i]])
                k=tmp
                if "Sizes" in currentProduct:
                    for size in currentProduct["Sizes"]:
                        if size[0]=='*': 
                            productsToBuy[k].append(size[1:])
                            k+=1
    return productsToBuy
                

if __name__ == "__main__":
    jsonObj=datascraper.retrieveJSON("productsBeta.json")
    arr=findChoosenItems(jsonObj)
    print(arr)
    #pool=Pool(processes=len(arr))
    #pool.map(addToBasket, arr)
    cookies=None
    driver=webdriver.Chrome(r"C:\Users\chewb\Desktop\chromedriver\chromedriver.exe")
    for product in arr:
       addToBasket(product,driver)
    driver.get("https://www.supremenewyork.com/checkout")