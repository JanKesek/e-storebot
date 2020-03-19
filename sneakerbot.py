from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(r"C:\Users\chewb\Desktop\chromedriver\chromedriver.exe")
driver.get("https://www.supremenewyork.com/shop/all/shirts")
#driver.find_element_by_xpath("//*[contains(text(),'Snakeskin Jacquard Shirt')]").click()
driver.find_element_by_xpath("//*[contains(text(),'Printed Plaid Shirt')]").click()
#driver.find_element_by_xpath("//fieldset[@id='add-remove-buttons']//input[@value='add to basket']").click()
#driver.find_element_by_css_selector("#add-remove-buttons > input")
a = driver.find_elements_by_class_name("button")
print(a)
time.sleep(2)
#for i in a:
 #       i.click()
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/form/fieldset[2]/input").click()      
#driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/form/fieldset[2]/input").click()
#driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/a[2]").click()
time.sleep(1)
driver.get("https://www.supremenewyork.com/checkout")

#/html/body/div[2]/div/div[2]/div/form/fieldset[2]/input
personalData=["FullName","Email","Phone","Address1","address2","Address3","City","PostCode","P","Number"]
i=0
while i <8:
        if i==3 or i==6:
                if i==3:
                        driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[1]/fieldset/div["+str(i+1)+"]/div[1]/input").send_keys(personalData[i])
                        driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[1]/fieldset/div["+str(i+1)+"]/div[2]/input").send_keys(personalData[i+1])
                        i+=2
                else:
                        driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[1]/fieldset/div["+str(i+1)+"]/div[1]/input").send_keys(personalData[i])
                        driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[1]/fieldset/div["+str(i+1)+"]/div[2]/label").send_keys(personalData[i+1]).send_keys(Keys.RETURN)
                        i+=2
        elif i==7:
                i+=1
        else:
                driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[1]/fieldset/div["+str(i+1)+"]/input").send_keys(personalData[i])
                i+=1


