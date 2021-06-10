import logging
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

logging.basicConfig(level=logging.INFO)


# https://github.com/operasoftware/operachromiumdriver/releases webdriver for Opera
driver = webdriver.Opera()
driver.get("https://vuetifyjs.com/en/components/menus/#usage")
driver.maximize_window()
DROPDOWN_BUTTON_SELECTOR = (
    "#usage > div > div.pa-4.v-sheet.theme--light.rounded > div > button > span"
)
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, DROPDOWN_BUTTON_SELECTOR))
).click()

DROPDOWN_MENU_SELECTOR = (
    "#app > div.v-menu__content.theme--light.menuable__content__active > div"
)
items = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, DROPDOWN_MENU_SELECTOR))
)
print(items.text)

time.sleep(10)
driver.close()
