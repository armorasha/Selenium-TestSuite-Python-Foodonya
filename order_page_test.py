import unittest
import time
from selenium.webdriver.common.keys import Keys  # for sending special keys like arrow down

from selenium.common.exceptions import NoSuchElementException

from selenium import webdriver

# these options for headless chrome
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')


class OrderPageTest(unittest.TestCase):

    def setUp(self):
        # self.driver_standard = webdriver.Chrome()  # standard chrome
        self.driver_headless = webdriver.Chrome(options=chrome_options)  # headless chrome
        # self.driver_standard.get('https://foodonya.com/php/order.php')
        self.driver_headless.get('https://foodonya.com/php/order.php')

    def test_ifOrderPageOpens(self):
        # def name must start with test_ inorder to the test to detect

        driv = self.driver_headless
        # converting self.driver_standard to driv for easy typing

        # time.sleep(3)

        self.assertIn("Traditional", driv.page_source)

        # self.driver.maximize_window()

    def test_ifSelectBtnWorks(self):
        driv = self.driver_headless
        # converting self.driver_standard to driv for easy typing

        elem = driv.find_element_by_xpath('//*[@id="collapse-1"]/div/div/div[3]/div/form/button')
        elem.click()

        self.assertIn("Kotto Pollo", driv.page_source)
        # page_source checks the whole page including html tags for the text "Kotto Pollo"

    def tearDown(self):
        # self.driver_standard.close()
        self.driver_headless.close()