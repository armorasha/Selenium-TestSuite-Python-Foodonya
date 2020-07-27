import unittest
import time
from selenium.webdriver.common.keys import Keys  # for sending special keys like arrow down

from selenium.common.exceptions import NoSuchElementException

from selenium import webdriver

# these options for headless chrome
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920,1080") # for disabling mobile states of hamburger menu, accordion


class OrderPageTest(unittest.TestCase):

    def setUp(self):
        # STANDARD CHROME
        # self.driver = webdriver.Chrome()
        # self.driver.get('https://foodonya.com/php/order.php')

        # HEADLESS CHROME
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('https://foodonya.com/php/order.php')

    def test_ifOrderPageOpens(self):
        # def name must start with test_ inorder to the test to detect

        driv = self.driver
        # converting self.driver to driv for easy typing

        # time.sleep(3)

        self.assertIn("Traditional", driv.page_source)

        # self.driver.maximize_window()

    def test_ifSelectBtnWorks(self):
        driv = self.driver
        # converting self.driver to driv for easy typing

        elem = driv.find_element_by_xpath('//*[@id="collapse-1"]/div/div/div[3]/div/form/button')
        elem.click()

        self.assertIn("Kotto Pollo", driv.page_source)
        # page_source checks the whole page including html tags for the text "Kotto Pollo"

    def tearDown(self):
        self.driver.close()
