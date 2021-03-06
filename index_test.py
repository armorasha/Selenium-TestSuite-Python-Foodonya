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


class IndexTestCase(unittest.TestCase):

    def setUp(self):
        # STANDARD CHROME
        # self.driver = webdriver.Chrome()
        # self.driver.get('https://foodonya.com')

        # HEADLESS CHROME
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('https://foodonya.com')

    def test_index_title(self):
        # def name must start with test_ inorder to the test to detect

        # driv = self.driver
        # converting self.driver to driv for easy typing
        # driv.get('https://foodonya.com')

        self.assertIn("Foodonya", self.driver.title)

        # time.sleep(5)
        # self.driver.maximize_window()

    def test_index_orderOnline_btn(self):
        driv = self.driver
        # converting self.driver to driv for easy typing

        elem = driv.find_element_by_id('orderOnline')
        elem.click()

        self.assertIn("Rustico", driv.page_source)
        # page_source checks the whole page including html tags for the text "Rustico"

    def test_index_aboutUs(self):
        driv = self.driver
        # converting self.driver to driv for easy typing

        elem = driv.find_element_by_xpath('/html/body/footer/div/div/div[3]/a')
        elem.click()

        self.assertIn("About Us", driv.page_source)

    def test_index_privacy(self):
        driv = self.driver
        # converting self.driver to driv for easy typing

        elem = driv.find_element_by_xpath('/html/body/footer/div/div/div[4]/a')
        elem.click()

        self.assertIn("Privacy Policy", driv.page_source)

    def test_index_terms(self):
        driv = self.driver
        # converting self.driver to driv for easy typing

        elem = driv.find_element_by_xpath('/html/body/footer/div/div/div[5]/a')
        elem.click()

        self.assertIn("Conditions", driv.page_source)

    def test_index_search_chicken(self):
        # THIS TEST WONT WORK IN HEADLESS CHROME, IF chrome_options.add_argument("--window-size=1920,1080") is
        # not set for disabling smaller mobile device display states of hamburger menu, accordion
        # In default headless chrome, the search bar may be inside the hamburger menu, so it cant be detected.

        driv = self.driver
        # converting self.driver to driv for easy typing

        # get search box html element
        elem = driv.find_element_by_id('search')
        # click on it
        elem.click()
        # type 'chicken' in it
        elem.send_keys('chicken')
        # click search button
        driv.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul/form/button').click()

        lists = driv.find_elements_by_class_name('card')  # elements- not element. this returns a list of items

        # print('list length: ', len(lists))
        self.assertEqual(9, len(lists)) # does the list has 9 cards?

        time.sleep(2)

    def test_index_search_cok(self):
        # THIS TEST WONT WORK IN HEADLESS CHROME, IF chrome_options.add_argument("--window-size=1920,1080") is
        # not set for disabling smaller mobile device display states of hamburger menu, accordion
        # In default headless chrome, the search bar may be inside the hamburger menu, so it cant be detected.

        driv = self.driver

        # get search box html element
        elem = driv.find_element_by_id('search')
        # click on it
        elem.click()
        # type 'chicken' in it
        elem.send_keys('cok')
        # click search button
        driv.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul/form/button').click()

        # lists = driv.find_elements_by_class_name('card')  # elements- not element. this returns a list of items
        # print('list length: ', len(lists))
        # self.assertEqual(0, len(lists)) # does the list has 0 cards? This works but better way of doing this is below

        # time.sleep(2)

        with self.assertRaises(NoSuchElementException):
            driv.find_element_by_class_name('card')  # does it raises NoSuch'card'ElementException for searching 'cok'?

        # This is the best way to check. Above test may raise a false positive.
        self.assertIn("Sorry, no item", driv.page_source)

    def tearDown(self):
        self.driver.close()

# TEST SUITE
# SEE: signup_login_test_suite.py for test suite example
# Created separate signup_login_test_suite.py file that only contains a particular test suite logic.
# For example, to test the membership functionalities alone, created a test suite that contains signup, login
#  and member-details-update tests alone. Run that test suite file to test only those functionalitites.
#
# Alternatively, you can create a directory containing those testcase files and run the whole directory. This method is
#  not very efficient but will do the job in simple cases.


# WORKS code.
# This is a test suite.
# Only these search tests will run if this index_test.py file is run from the command prompt
# That's because, when this file is called from the command prompt as
#
#  C:\Users\000930322\Downloads\Web development\Foodonya Python Selenium Tests>python index_test.py
#
#  the main() method will run. In this file there is no main method,
#  so instead the suite() method will be run by the runner.


def suite():
    suite = unittest.TestSuite()
    suite.addTest(IndexTestCase('test_index_search_chicken')) # running only selected tests
    suite.addTest(IndexTestCase('test_index_search_cok'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
