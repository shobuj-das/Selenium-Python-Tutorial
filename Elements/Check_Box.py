import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://demoqa.com/checkbox")
driver.find_element(By.XPATH, "//span[@class='rct-title' and text()='Home']").click()
time.sleep(2)
print("Home :", driver.find_element(By.XPATH, "//span[@class='rct-title' and text()='Home']").is_selected())
driver.find_element(By.XPATH, "//button[@title='Expand all']").click()
print("Notes: ", driver.find_element(By.XPATH, "//span[@class='rct-title' and text()='Notes']").is_selected())
time.sleep(2)
driver.find_element(By.XPATH, "//span[@class='rct-title' and text()='Notes']").click()
print("Notes: ", driver.find_element(By.XPATH, "//span[@class='rct-title' and text()='Notes']").is_selected())
time.sleep(2)
driver.find_element(By.XPATH, "//span[@class='rct-title' and text()='Notes']").click()
print("Notes: ", driver.find_element(By.XPATH, "//span[@class='rct-title' and text()='Notes']").is_selected())
driver.quit()