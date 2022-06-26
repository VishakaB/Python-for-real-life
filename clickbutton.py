from selenium import webdriver
from selenium.webdriver.common.by import By

import time
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)  # Make sure you have YOUR path to the chromedriver
driver.get("https://ceb.lk/")

time.sleep(2)

try:
    element = WebDriverWait(driver).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Click here"))
    )
    element.click()

except:
    driver.quit()