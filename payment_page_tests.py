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


class PaymentTestCase(unittest.TestCase):

    def setUp(self):
        # STANDARD CHROME
        self.driver = webdriver.Chrome()
        self.driver.get('https://foodonya.com/php/order.php')

        # HEADLESS CHROME
        # self.driver = webdriver.Chrome(options=chrome_options)
        # self.driver.get('https://foodonya.com/php/order.php')

    def test_NoDirectAccessToPaymentPage(self):
        driv1 = self.driver
        driv1.get('https://foodonya.com/php/payment.php')

        self.assertNotIn("payment.php", driv1.current_url)
        # No direct access to payment_page? by checking the url has no 'payment.php'

    def test_ifPlaceOrderBtnWorks_guest(self): # condition: if a member logged in, this fails
        driv = self.driver

        time.sleep(2)

        select = driv.find_element_by_xpath('//*[@id="collapse-1"]/div/div/div[3]/div/form/button')
        select.click()
        # Selects Kotto Pollo from order page and goes to select page

        time.sleep(2)

        add_qty = driv.find_element_by_xpath('/html/body/form/div/div/button[2]')
        add_qty.click()
        # adds one to qty

        time.sleep(2)

        add_to_cart = driv.find_element_by_xpath('/html/body/form/div/div/button[3]')
        add_to_cart.click()
        # adds Kotto Pollo to cart

        time.sleep(2)

        proceed_to_checkout = driv.find_element_by_xpath('/html/body/div/div/form/button')
        proceed_to_checkout.click()
        # clicks proceed to checkout button

        # self.assertIn("payment.php", driv.current_url)
        # Arrived in payment_page? by checking the url has 'payment.php'

        time.sleep(3)

        # Arrived in payment_page
        guest1 = {"guestEmail": "armi@yahee.ccc", "cust_name": "Raji Pali", "street": "100 Sth rd", "suburb": "Roarx",
                  "postcode": "5559", "phone": "0444111222"}

        for key, value in guest1.items():
            driv.find_element_by_id(key).send_keys(value)

        self.assertIn("$13.90", driv.page_source)


        self.assertIn("payment.php", driv.current_url)

    def tearDown(self):
        time.sleep(10)
        self.driver.close()

