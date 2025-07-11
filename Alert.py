import time
from re import search
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/alerts")
driver.find_element(By.ID, "promtButton").click()
WebDriverWait(driver,10).until(expected_conditions.alert_is_present())
alert = driver.switch_to.alert
alert.send_keys("demo text")
alert.accept()
result = WebDriverWait(driver,10).until(expected_conditions.text_to_be_present_in_element((By.ID, "promptResult"),"demo text"))
# result = driver.find_element(By.ID, "promptResult").text
assert "demo text" in result, "Not found"
print("Successful")

driver.quit()