from re import search
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com/")
sleep(2)
print(driver.title)
print(driver.current_url)

search_box = (By.ID,"input")
driver.find_element(*search_box).send_keys("first script")
sleep(2)

driver.quit()
