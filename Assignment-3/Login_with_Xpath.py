import time
from re import search
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

URl = "https://www.saucedemo.com/"

# --- credentials
user_name = "standard_user"
password = "secret_sauce"

#---- locators
username_field = "//input[@id='user-name']"
password_field = "//input[@id='password']"
login_button = "//input[@id='login-button']"

driver.get(URl)
driver.find_element(By.XPATH,username_field).send_keys(user_name)
driver.find_element(By.XPATH, password_field).send_keys(password)
driver.find_element(By.XPATH, login_button).click()

time.sleep(2)
driver.quit()