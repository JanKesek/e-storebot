from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time

class Test(unittest.TestCase):
    def testCanSolveCaptcha(self):
        url = 'https://www.google.com/recaptcha/api2/demo'
        driver=webdriver.Chrome(r"C:\Users\chewb\Desktop\chromedriver\chromedriver.exe")
        driver.get(url)
        api_key = '96b24a9a9561538e0d10d18cd26f4f50'
        time.sleep(2)
        recaptcha_demo= driver.find_element_by_id('recaptcha-demo')
        site_key = recaptcha_demo.get_attribute('data-sitekey')
        print(site_key)
        client = AnticaptchaClient(api_key)
        task = NoCaptchaTaskProxylessTask(url, site_key)
        job = client.createTask(task)
        job.join()
        captcha_response = job.get_solution_response()
        print("FINISHED EXECUTING CAPTCHA", captcha_response)
        driver.execute_script('document.getElementById("g-recaptcha-response").innerHTML = "%s"' % captcha_response)
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="recaptcha-demo-submit"]').click()
        time.sleep(5)
        
if __name__=='__main__':
    unittest.main(warnings='ignore')