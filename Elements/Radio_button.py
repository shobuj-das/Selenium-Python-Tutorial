from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://demoqa.com/radio-button")
driver.find_element(By.ID,"yesRadio").click()
print("Yes button is clicked: ", driver.find_element(By.ID,"yesRadio").is_selected())
print("Text success: ", )