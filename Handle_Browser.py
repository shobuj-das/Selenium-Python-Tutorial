import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://w3schools.com/")
driver.switch_to.new_window('tab')
time.sleep(3)

driver.get("https://google.com/")
time.sleep(3)

tabs = list(driver.window_handles)
print("-- tabs handles: ",tabs)

driver.switch_to.window(tabs[0])  # facebook
time.sleep(2)
driver.close()  # facebook
driver.switch_to.window(tabs[1])

driver.switch_to.new_window('window')
driver.get("https://github.com/")
time.sleep(2)

windows = list(driver.window_handles)
print("-- windows handles: ",windows)

driver.switch_to.window(windows[0])  # google
driver.close() # google

time.sleep(3)
driver.quit()
