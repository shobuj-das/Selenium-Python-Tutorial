import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def create_and_handle_tabs():
    driver.get("https://w3schools.com/")
    driver.switch_to.new_window('tab')  # creates a new tab
    time.sleep(3)

    driver.get("https://google.com/") # load google in the new tab
    time.sleep(3)

    tabs = list(driver.window_handles)  # store tabs handle in a list
    print("-- tabs handles: ", tabs)  # print the handle code

    driver.switch_to.window(tabs[0])  # w3schools
    time.sleep(2)
    driver.close()  # w3schools
    driver.switch_to.window(tabs[1])  # switch to second tab

def create_and_handle_window():
    driver.switch_to.new_window('window') # creates a new window
    driver.get("https://github.com/")  # load github in the new window
    time.sleep(2)

    windows = list(driver.window_handles)
    print("-- windows handles: ", windows)

    driver.switch_to.window(windows[0])  # google
    driver.close()  # google

    time.sleep(3)


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

create_and_handle_tabs()
create_and_handle_window()
driver.quit()
