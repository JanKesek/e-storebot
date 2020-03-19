import unittest
import sys
sys.path.append("..")
import datascraper

class Test(unittest.TestCase):
    def testJSONHasAllProducts(self):
        urlTree=datascraper.getAllItemsURLS()
        jsonObj=datascraper.makeJSON(urlTree)
        numberOfProducts=0
        for category in jsonObj:
            for product in jsonObj[category]:
                numberOfProducts+=len(jsonObj[category][product])
        self.assertEqual(len(urlTree), numberOfProducts)
    def testArrayDoesNotHaveDuplicates(self):
        urlTree=datascraper.getAllItemsURLS()
        uniqueProducts=[]
        for elem in urlTree:
            uniqueProducts.append(elem[2]+elem[3])
        self.assertEqual(len(uniqueProducts), len(set(uniqueProducts)))
    def testConvertJSONToArrayCheckUniqueness(self):
        urlTree=datascraper.getAllItemsURLS()
        jsonObj=datascraper.makeJSON(urlTree)
        lst=[]
        for category in jsonObj:
            for product in jsonObj[category]:
                for el in jsonObj[category][product]:
                    lst.append(product+el)
        print(len(lst))
        self.assertEqual(len(lst), len(set(lst)))
if __name__=='__main__':
    unittest.main(warnings='ignore')