import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# ------------ Form information
user_full_name = "Shobuj Das"
user_email = "shobuj@das.com"
current_address = '''Basa-101
Road-202
Mirpur-303
Dhaka, Bangladesh'''
permanent_address = '''Basa-505
Road-307
Mirpur-999
Cumilla, Bangladesh'''
URL = "https://demoqa.com/text-box"

# -------- Locators
homepage_elements_button = (By.XPATH, "//div[@class='card-body']/h5[text()='Elements']")
text_box_button = (By.XPATH, "//span[@class='text' and text()='Text Box']")

full_name_field = (By.ID, "userName")
email_field = (By.ID, "userEmail")
current_address_field = (By.ID, "currentAddress")
permanent_address_field = (By.ID, "permanentAddress")
submit_button = (By.ID, "submit")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get(URL)
# driver.find_element(*homepage_elements_button).click()
# driver.find_element(*text_box_button).click()
driver.find_element(*full_name_field).send_keys(user_full_name)
time.sleep(0.5)
driver.find_element(*email_field).send_keys(user_email)
time.sleep(0.5)
driver.find_element(*current_address_field).send_keys(current_address)
time.sleep(0.5)
driver.find_element(*permanent_address_field).send_keys(permanent_address)
time.sleep(2)
driver.find_element(*submit_button).click()
time.sleep(1)
