import unittest
import time
from selenium.webdriver.common.keys import Keys  # for sending special keys like arrow down

from selenium.common.exceptions import NoSuchElementException

from selenium import webdriver


class PaymentTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # standard chrome
        self.driver.get('https://foodonya.com/php/payment.php')

    def test_ifPaymentPageDontOpens(self):
        # def name must start with test_ inorder to the test to detect

        driv = self.driver
        # converting self.driver to driv for easy typing
        # time.sleep(2)

        self.assertNotIn("Accepted payment methods", driv.page_source)

    def test_ifPlaceOrderBtnWorks(self):
        driv = self.driver
        # converting self.driver to driv for easy typing

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

        item_text = driv.find_element_by_tag_name('td').text
        self.assertEqual("Kotto Pollo", item_text)
        # checking to see if Kotto Pollo has been added in view_cart page by checking the tag <td> has 'Kotto Pollo'.

    def tearDown(self):
        self.driver.close()

