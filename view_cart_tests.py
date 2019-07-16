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


class ViewCartTestCase(unittest.TestCase):

    def setUp(self):
        # STANDARD CHROME
        # self.driver = webdriver.Chrome()
        
        # HEADLESS CHROME
        self.driver = webdriver.Chrome(options=chrome_options)

    def test_ifViewCartOpens(self):
        driv1 = self.driver
        driv1.get('https://foodonya.com/php/view_cart.php')

        self.assertIn("Cart", driv1.page_source)

    def test_ifProceedToCheckoutBtnWorks(self):
        driv2 = self.driver
        self.driver.get('https://foodonya.com/php/order.php')

        select = driv2.find_element_by_xpath('//*[@id="collapse-1"]/div/div/div[3]/div/form/button')
        select.click()
        # Selects Kotto Pollo from order page and goes to select page

        add_qty = driv2.find_element_by_xpath('/html/body/form/div/div/button[2]')
        add_qty.click()
        # adds one to qty

        add_to_cart = driv2.find_element_by_xpath('/html/body/form/div/div/button[3]')
        add_to_cart.click()
        # adds Kotto Pollo to cart

        proceed_to_checkout = driv2.find_element_by_xpath('/html/body/div/div/form/button')
        proceed_to_checkout.click()
        # clicks proceed to checkout button

        self.assertIn("payment.php", driv2.current_url)
        # Arrived in payment_page? by checking the url has 'payment.php'

    def tearDown(self):
        # time.sleep(2)
        self.driver.close()
