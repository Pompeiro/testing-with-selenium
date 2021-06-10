import logging
import time

from selenium import webdriver

logging.basicConfig(level=logging.INFO)

REQUIRED_CHECKBOXES = ["Chips", "Deletable Chips"]
REQUIRED_COUNTRY = "Palau"


# https://github.com/operasoftware/operachromiumdriver/releases webdriver for Opera
driver = webdriver.Opera()
driver.get("https://vuetifyjs.com/en/components/autocompletes/")
driver.maximize_window()


CHECKBOX_OPTIONS_XPATH = '//*[@id="usage"]/div/div/div/div[2]/div[2]/div'
checkbox_options = driver.find_element_by_xpath(CHECKBOX_OPTIONS_XPATH)
checkbox_options_splitted = checkbox_options.text.split("\n")
for i, option in enumerate(checkbox_options_splitted):
    print(option)
    if option in REQUIRED_CHECKBOXES:
        # i + 1 because first option start from 1 and enumerate starts from 0
        REQUIRED_CHECK_BOX_XPATH = (
            '//*[@id="usage"]/div/div/div/div[2]/div[2]/div/div/div['
            + str((i + 1))
            + "]/div/div/div/div"
        )
        driver.find_element_by_xpath(REQUIRED_CHECK_BOX_XPATH).click()

AUTOCOMPLETION_XPATH = '//*[@id="usage"]/div/div/div/div[1]/div[2]/div'
driver.find_element_by_xpath(AUTOCOMPLETION_XPATH).click()
time.sleep(1.5)
COUNTRY_INPUT_FIELD_XPATH = '//*[@id="input-743"]'
driver.find_element_by_xpath(COUNTRY_INPUT_FIELD_XPATH).send_keys("P")

time.sleep(1.5)
COUNTRY_LIST_XPATH = '//*[@id="list-743"]'
country_list_in_autocompletion = driver.find_element_by_xpath(COUNTRY_LIST_XPATH)
country_list_in_autocompletion_splitted = country_list_in_autocompletion.text.split(
    "\n"
)

for i, country in enumerate(country_list_in_autocompletion_splitted):
    print(country)
    if country == REQUIRED_COUNTRY:
        REQUIRED_COUNTRY_XPATH = '//*[@id="list-item-769-' + str(i) + '"]/div'
        driver.find_element_by_xpath(REQUIRED_COUNTRY_XPATH).click()
        break

time.sleep(5)
COUNTRY_TO_DELETE_XPATH = '//*[@id="usage"]/div/div/div/div[1]/div[2]/div/div/div[1]/div[1]/div[1]/span/span/button'
driver.find_element_by_xpath(COUNTRY_TO_DELETE_XPATH).click()

time.sleep(10)
driver.close()
