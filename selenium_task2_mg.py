import logging
import time

from selenium import webdriver

FIRST_NAME = "Maciej"
LAST_NAME = "Gojlik"
EMAIL = "maciejgojlik@wp.pl"

# https://github.com/operasoftware/operachromiumdriver/releases webdriver for Opera
driver = webdriver.Opera()
driver.get("https://vuetifyjs.com/en/components/forms/#usage")
driver.maximize_window()
FIRST_NAME_INPUT_FIELD_XPATH = '//*[@id="input-572"]'
LAST_NAME_INPUT_FIELD_XPATH = '//*[@id="input-575"]'
EMAIL_INPUT_FIELD_XPATH = '//*[@id="input-578"]'

time.sleep(2)
driver.find_element_by_xpath(FIRST_NAME_INPUT_FIELD_XPATH).send_keys(FIRST_NAME)
driver.find_element_by_xpath(LAST_NAME_INPUT_FIELD_XPATH).send_keys(LAST_NAME)
driver.find_element_by_xpath(EMAIL_INPUT_FIELD_XPATH).send_keys(EMAIL)

time.sleep(10)
driver.close()
