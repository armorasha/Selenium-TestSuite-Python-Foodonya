import time
import unittest

from selenium import webdriver as wd


class FirstTest(unittest.TestCase):
    def test_first_selenium_test(self):
        self.driver = wd.Chrome()

        self.driver.get('https://foodonya.com')

#        self.driver.find_element_by_xpath('//*[@id="orderOnline"]').click()
        elem = self.driver.find_element_by_id('search')

        elem.click()
        elem.send_keys('chicken')
        self.driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul/form/button').click()

        #here assert the results for chicken or chocken

#        time.sleep(5)
#        self.driver.maximize_window()
        self.driver.close()
