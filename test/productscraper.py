import unittest
import sys
import os
import requests
sys.path.append("..")
import datascraper

class Test(unittest.TestCase):
    def setUp(self):
        self.jsonObj=datascraper.retrieveJSON(os.getcwd()+'\..\productsBeta.json')
    @unittest.skip
    def testJSONHasAllProducts(self):
        urlTree=datascraper.getAllItemsURLS()
        numberOfProducts=0
        for category in self.jsonObj:
            for product in self.jsonObj[category]:
                numberOfProducts+=len(self.jsonObj[category][product]["Colours"])
        self.assertEqual(len(urlTree), numberOfProducts)
    @unittest.skip
    def testArrayDoesNotHaveDuplicates(self):
        urlTree=datascraper.getAllItemsURLS()
        uniqueProducts=[]
        for elem in urlTree:
            uniqueProducts.append(elem[2]+elem[3])
        self.assertEqual(len(uniqueProducts), len(set(uniqueProducts)))
    @unittest.skip
    def testConvertJSONToArrayCheckUniqueness(self):
        urlTree=datascraper.getAllItemsURLS()
        lst=[]
        for category in self.jsonObj:
            for product in self.jsonObj[category]:
                for el in self.jsonObj[category][product]:
                    lst.append(product+el)
        print(len(lst))
        self.assertEqual(len(lst), len(set(lst)))
    def testAllMenuURLs200(self):
        for category in self.jsonObj:
            for product in self.jsonObj[category]:
                for url in self.jsonObj[category][product]["URLs"]:
                    req=requests.get(url)
                    self.assertEqual(req.status_code, 200)
    @unittest.skip
    def testValuesDoesNotBeginsWithStandardStarChar(self):
        for category in self.jsonObj:
            for product in self.jsonObj[category]:
                for style in self.jsonObj[category][product]["Colours"]:
                    self.assertNotEqual(style[0],"*")
if __name__=='__main__':
    unittest.main(warnings='ignore')