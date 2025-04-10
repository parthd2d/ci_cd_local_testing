import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

wait=WebDriverWait(driver,5)

try:
    driver.maximize_window()

    driver.get('http://localhost:8000')

    test_page=wait.until(EC.element_to_be_clickable((By.XPATH,"//a[text()='index.html']")))
    test_page.click()

    link=wait.until(EC.visibility_of_element_located((By.ID,'old-link')))
    link.click()

    time.sleep(3)

finally:
    # Stop the driver
    driver.quit()