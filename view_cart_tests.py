import unittest
import time
from selenium.webdriver.common.keys import Keys  # for sending special keys like arrow down

from selenium.common.exceptions import NoSuchElementException

from selenium import webdriver

# these options for headless chrome
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')


class ViewCartTestCase(unittest.TestCase):

    def setUp(self):
        # STANDARD CHROME
        # self.driver_standard = webdriver.Chrome()
        # self.driver_standard.get('https://foodonya.com/php/order.php')

        # HEADLESS CHROME
        self.driver_headless = webdriver.Chrome(options=chrome_options)
        self.driver_headless.get('https://foodonya.com/php/order.php')

    def test_NoDirectAcessToViewCart(self):
        driv = self.driver_headless
        # time.sleep(2)
        self.assertNotIn("Proceed to Checkout", driv.page_source)

    def test_ifProceedToCheckoutBtnWorks(self):
        driv = self.driver_headless

        select = driv.find_element_by_xpath('//*[@id="collapse-1"]/div/div/div[3]/div/form/button')
        select.click()
        # Selects Kotto Pollo and goes to select page

        add_qty = driv.find_element_by_xpath('/html/body/form/div/div/button[2]')
        add_qty.click()
        # adds one to qty

        add_to_cart = driv.find_element_by_xpath('/html/body/form/div/div/button[3]')
        add_to_cart.click()
        # adds Kotto Pollo to cart

        proceed_to_checkout = driv.find_element_by_xpath('/html/body/div/div/form/button')
        proceed_to_checkout.click()
        # clicks proceed to checkout button

        self.assertIn("payment.php", driv.current_url)
        # checking to see if payment_page has been arrived by checking the url has 'payment.php'

        # time.sleep(2)

    def tearDown(self):
        # self.driver_standard.close()
        self.driver_headless.close()
