import webdriver_manager
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://demoqa.com/buttons")

double_click_button = (By.ID, "doubleClickBtn")
right_click_button = (By.ID, "rightClickBtn")
click_me_button = (By.ID, "kwpJf")

actions = ActionChains(driver)
double_element = driver.find_element(*double_click_button)
actions.double_click(double_element).perform()
double_mgs = driver.find_element(By.ID, "doubleClickMessage").text
assert "double click" in double_mgs, "Text not matched"

actions.context_click(driver.find_element(*right_click_button)).perform()

driver.quit()