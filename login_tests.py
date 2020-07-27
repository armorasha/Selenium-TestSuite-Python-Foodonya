import unittest
import time

import mysql.connector
# Community version of PyCharm doesnt have support for database handling.
# Use Python IDLE if you want to use and test mysql databases.

from selenium.webdriver.common.keys import Keys  # for sending special keys like arrow down

from selenium.common.exceptions import NoSuchElementException

from selenium import webdriver

# these options for headless chrome
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920,1080") # for disabling mobile states of hamburger menu, accordion


class LoginTestCase(unittest.TestCase):

    def setUp(self):
        # STANDARD CHROME
        # self.driver = webdriver.Chrome()
        # self.driver.get('https://foodonya.com/php/login.php')

        # HEADLESS CHROME
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('https://foodonya.com/php/login.php')

    def test_ifLoginWorks(self): # condition: if a member already logged in, this test fails
        driv = self.driver

        member14 = {"email": "cust14@hmail.com", "psw": "14ssssss"}

        for key, value in member14.items():
            driv.find_element_by_id(key).send_keys(value)

        login_btn = driv.find_element_by_xpath('//*[@id="captchaBtn"]')
        login_btn.click()
        # clicks member login button

        self.assertIn("Welcome Back", driv.page_source)
        self.assertIn("Vinod Kumar", driv.page_source)
        # checking to see if customer logged in

    def test_ifLoginWorks_newSignup(self): # this test is for the test suite in signup_login_test_suite.py
        # condition: if a member already logged in, this test fails

        driv = self.driver

        member15 = {"email": "cust15@hmail.com", "psw": "15ssssss"}

        for key, value in member15.items():
            driv.find_element_by_id(key).send_keys(value)

        login_btn = driv.find_element_by_xpath('//*[@id="captchaBtn"]')
        login_btn.click()
        # clicks member login button

        self.assertIn("Welcome Back", driv.page_source)
        self.assertIn("Raji Pali", driv.page_source)
        # checking to see if customer logged in

    def tearDown(self):
        time.sleep(3)
        self.driver.close()

