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


class SignupTestCase(unittest.TestCase):

    def setUp(self):
        # STANDARD CHROME
        # self.driver = webdriver.Chrome()
        # self.driver.get('https://foodonya.com/php/signup.php')

        # HEADLESS CHROME
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('https://foodonya.com/php/signup.php')

    def test_ifSignupWorks(self): # condition: if a member already logged in, this test fails
        driv = self.driver

        member1 = {"email": "cust15@hmail.com", "psw": "15ssssss", "pswRepeat": "15ssssss", "cust_name": "Raji Pali",
                   "street": "100 Sth rd", "suburb": "Roarx", "postcode": "5559", "phone": "0444111222"}

        for key, value in member1.items():
            driv.find_element_by_id(key).send_keys(value)

        state_dropdown = driv.find_element_by_xpath('//*[@id="state"]/option[2]')
        state_dropdown.click()
        # selects option 2- NSW in the dropdown button

        register_btn = driv.find_element_by_xpath('//*[@id="captchaBtn"]')
        register_btn.click()
        # clicks new member register button

        self.assertIn("Hello", driv.page_source)
        self.assertIn("Raji Pali", driv.page_source)
        # checking to see if customer logged in

    def tearDown(self):
        time.sleep(3)
        self.driver.close()

