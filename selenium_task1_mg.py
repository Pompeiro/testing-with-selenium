import logging
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

logging.basicConfig(level=logging.INFO)

REQUIRED_ITEM = "Fizz"


# https://github.com/operasoftware/operachromiumdriver/releases webdriver for Opera
driver = webdriver.Opera()
driver.get("https://vuetifyjs.com/en/components/selects/")
driver.maximize_window()

OUTLINED_STYLE_DROPDOWN_SELECTOR = "#usage > div > div.pa-4.v-sheet.theme--light.rounded > div > div > div:nth-child(3) > div > div > div.v-input__slot > div.v-select__slot > div.v-select__selections"
# https://stackoverflow.com/a/59132328
# https://stackoverflow.com/questions/59130200/selenium-wait-until-element-is-present-visible-and-interactable
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, OUTLINED_STYLE_DROPDOWN_SELECTOR))
).click()

OUTLINED_STYLE_LIST_SELECTOR = "#list-646"
items = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, OUTLINED_STYLE_LIST_SELECTOR))
)
items_splitted = items.text.split()
logging.info(
    "Loop over items inside dropdown menu and check for required item: %s",
    REQUIRED_ITEM,
)
for i, item in enumerate(items_splitted):
    logging.info("%s", item)
    if item == REQUIRED_ITEM:
        print("Found {} on index: {}".format(REQUIRED_ITEM, i))
        required_item_index = i
        break

try:
    OUTLINED_STYLE_REQUIRED_ITEM_SELECTOR = (
        "#list-item-783-" + str(required_item_index) + " > div > div"
    )
except NameError:
    logging.error(
        "Fizz not found inside items_splitted: %s. Check selector!", items_splitted
    )
    raise
driver.find_element_by_css_selector(OUTLINED_STYLE_REQUIRED_ITEM_SELECTOR).click()

time.sleep(5)
driver.close()
