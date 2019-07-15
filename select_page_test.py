import unittest
from selenium.webdriver.common.keys import Keys  # for sending special keys like arrow down

from selenium.common.exceptions import NoSuchElementException

from selenium import webdriver

# these options for headless chrome
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')


class IndexTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # standard chrome
        # self.driver = webdriver.Chrome(options=chrome_options)  # headless chrome
        self.driver.get('https://foodonya.com/php/order.php')

    def test_ifSelectPageDontOpens(self):
        # def name must start with test_ inorder to the test to detect

        driv = self.driver
        # converting self.driver to driv for easy typing

        self.assertNotIn("Add to Cart", driv.page_source)

    def test_ifAddToCartBtnWorks(self):
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

        # heading_text = driv.find_element_by_xpath('/html/body/div/h4').text
        # self.assertEqual("Cart", heading_text)
        # checking to see if view_page has been arrived by checking the heading has 'Cart'. Better way below.

        self.assertIn("view_cart.php", driv.current_url)
        # checking to see if view_page has been arrived by checking the heading has 'Cart'

        item_text = driv.find_element_by_tag_name('td').text
        self.assertEqual("Kotto Pollo", item_text)
        # checking to see if Kotto Pollo has been added in view_cart page by checking the tag <td> has 'Kotto Pollo'.

    def tearDown(self):
        self.driver.close()

