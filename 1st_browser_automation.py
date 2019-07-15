import time

from selenium import webdriver as wd

driver = wd.Chrome()

driver.get('https://foodonya.com')

#driver.find_element_by_xpath('//*[@id="orderOnline"]').click()

driver.find_element_by_id('search').click()
driver.find_element_by_id('search').send_keys('chicken')
driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul/form/button').click()

time.sleep(5)
#driver.maximize_window()
driver.close()
