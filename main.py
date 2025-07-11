import time
from re import search
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


# Open a new tab and navigate to w3schools

driver.get("https://www.w3schools.com")
driver.switch_to.new_window('tab')
time.sleep(2)
driver.get("https://www.google.com")
# Get all window handles as a list
tabs = list(driver.window_handles)

# Switch to the first tab (index 0) and close it
driver.switch_to.window(tabs[0])
driver.close()
time.sleep(2)

# Switch to the second tab (index 1)
driver.switch_to.window(tabs[1])

# Open a new window and navigate to LinkedIn
driver.switch_to.new_window('window')
driver.get("https://www.linkedin.com")
time.sleep(2)