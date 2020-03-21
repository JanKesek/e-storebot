import requests
import json
from bs4 import BeautifulSoup
def getURLSoup(url):
    html=requests.get(url)
    return BeautifulSoup(html.text)
def getAllItemsURLS():
    allProducts=requests.get("https://www.supremenewyork.com/shop/all")
    soup = BeautifulSoup(allProducts.text)
    urlTrees=[]
    productTypes=['jackets','shirts','tops-sweaters','sweatshirts','pants','shorts','t-shirts','hats','bags','accessories','shoes','skate']
    for a in soup.find_all('a', href=True):
        tree=a['href'][1:].split("/")
        if len(tree)==4 and tree[1] in productTypes: urlTrees.append(tree)
    return urlTrees
def makeJSON(arr):
    jsonObj={ arr[0][1]: {} }
    for elem in arr:
        if elem[1] not in jsonObj:
            jsonObj[elem[1]]={}
        if elem[2] not in jsonObj[elem[1]]:
            jsonObj[elem[1]][elem[2]]=[elem[3]]
        else:
            jsonObj[elem[1]][elem[2]].append(elem[3])
    return jsonObj
def saveJSON(filename,jsonObj):
    with open(filename, 'w') as of:
        json.dump(jsonObj, of, indent=4)
def retrieveJSON(filename):
    with open(filename) as of:
        return json.load(of)
def apiToNames(jsonObj):
    data={}
    globalUrl="https://www.supremenewyork.com/shop/"
    for category in jsonObj:
        data[category]={}
        for product in jsonObj[category]:
            soup=getURLSoup(globalUrl+category+"/"+product)
            productTitle=soup.find("h1", {"class":"protect"}).text.encode('ascii','ignore').decode('utf-8')
            data[category][productTitle]={
                "Colours":[],
                "URLs":[]
            }
            for col in jsonObj[category][product]:
                styleURL=globalUrl+category+"/"+product+"/"+col
                soupStyle=getURLSoup(styleURL)
                data[category][productTitle]["Colours"].append(soupStyle.find("p",{"class":"style protect"}).text.encode('ascii','ignore').decode('utf-8'))
                data[category][productTitle]["URLs"].append(styleURL)
            data[category][productTitle]["Price"]=soup.find("span",{"data-currency":"EUR","itemprop":"price"}).text.encode('ascii','ignore').decode('utf-8')
            sizes=soup.find("select",{"id":"size","name":"size"})
            if sizes!=None:
                sizes=sizes.findAll("option")
                data[category][productTitle]["Sizes"]=[size.text for size in sizes]
            data[category][productTitle]["BuyIt"]=False
    return data        

if __name__ == "__main__":
    #arr=getAllItemsURLS()
    #print(arr)
    #num=0
    #jsonObj=makeJSON(arr)
    #saveJSON("productsAlpha.json", jsonObj)
    basicJson=retrieveJSON("productsAlpha.json")
    advJSON=apiToNames(basicJson)
    print(advJSON)
    try:
        saveJSON("productsBeta.json", advJSON)
    except TypeError as te:
        print(te)