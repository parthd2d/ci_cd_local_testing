import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from dotenv import load_dotenv
import os
from selenium.webdriver.chrome.options import Options

# driver = webdriver.Chrome()

load_dotenv()
BROWSERSTACK_USERNAME = os.environ.get("BROWSERSTACK_USERNAME") or "BROWSERSTACK_USERNAME"
BROWSERSTACK_ACCESS_KEY = os.environ.get("BROWSERSTACK_ACCESS_KEY") or "BROWSERSTACK_ACCESS_KEY"
URL = "https://hub.browserstack.com/wd/hub"

bstack_options = {
    "os" : "OS X",
    "osVersion" : "Monterey",
    "buildName" : "testing",
    "sessionName" : "cicd testing",
    "userName": BROWSERSTACK_USERNAME,
    "accessKey": BROWSERSTACK_ACCESS_KEY,
    "local" : "true",
    "localIdentifier":"parth-testing"
}
bstack_options["source"] = "python:sample-main:v1.0"
options = Options()
options.set_capability('bstack:options', bstack_options)
driver = webdriver.Remote(
    command_executor=URL,
    options=options)

wait=WebDriverWait(driver,5)

try:
    driver.maximize_window()

    driver.get('http://localhost:8000')

    test_page=wait.until(EC.element_to_be_clickable((By.XPATH,"//a[text()='page.html']")))
    test_page.click()

    link=wait.until(EC.visibility_of_element_located((By.ID,'old-link')))
    link.click()

    time.sleep(3)

finally:
    # Stop the driver
    driver.quit()