import tempfile
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    # 1. Create Chrome Options
    chrome_options = Options()

    # 2. Launch in incognito mode (no history/cookies)
    chrome_options.add_argument("--incognito")

    # 3. Disable caching
    chrome_options.add_argument("--disk-cache-size=0")
    chrome_options.add_argument("--disable-application-cache")
    chrome_options.add_argument("--disable-cache")

    # 4. Use a temporary user data directory (to ensure fresh memory/cache)
    temp_user_data_dir = tempfile.mkdtemp()
    chrome_options.add_argument(f"--user-data-dir={temp_user_data_dir}")

    # 5. Disable password manager popups (optional, for automation)
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service,options=chrome_options)
    driver.maximize_window()
    return driver


def log_in():
    driver.get("https://www.saucedemo.com/")
    driver.find_element(*username_field).send_keys(username)
    driver.find_element(*password_field).send_keys(user_password)
    driver.find_element(*login_button).click()
    assert "https://www.saucedemo.com/inventory.html" in driver.current_url, "login failed"

def add_to_cart():
    driver.find_element(*product_1_add_to_cart_button).click()
    assert "1" in driver.find_element(*cart_badge).text, "Product not added"

def add_to_cart_by_product_name():
    product_name_list = driver.find_elements(*inventory_item_name)
    print(f"total : ", len(product_name_list))
    cart_index = 1
    for element in product_name_list:
        name = element.text
        print(name)
        if name == product_name:
            break
        cart_index += 1

    add_to_cart_button = add_to_cart_xpath + "["+str(cart_index)+"]"
    driver.find_element(By.XPATH, add_to_cart_button).click()
    time.sleep(3)

def check_out():
    driver.find_element(*cart_button).click()
    time.sleep(3)
    assert "https://www.saucedemo.com/cart.html" == driver.current_url, "Not redirect"
    driver.find_element(*check_out_button).click()
    time.sleep(2)

def enter_user_information():
    driver.find_element(*first_name_field).send_keys("Shobuj")
    driver.find_element(*last_name_field).send_keys("Das")
    driver.find_element(*zip_code_field).send_keys("12345")
    driver.find_element(*continue_button).click()
    time.sleep(1)
    assert "https://www.saucedemo.com/checkout-step-two.html" == driver.current_url, "info added"
    driver.find_element(*finish_button).click()
    time.sleep(1)
    assert "https://www.saucedemo.com/checkout-complete.html" == driver.current_url


# -------------- Locators ---------------------------------------
#---- login page locators ------
username_field = (By.ID, "user-name")
password_field = (By.ID, "password")
login_button = (By.ID, "login-button")
username = "standard_user"
user_password = "secret_sauce"

# ---- inventory page locators
product_1_add_to_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")
cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
cart_button = (By.CLASS_NAME, "shopping_cart_link")
product_name = "Sauce Labs Fleece Jacket"
inventory_item_name = (By.CLASS_NAME, "inventory_item_name ")
add_to_cart_xpath = "(//button[@class='btn btn_primary btn_small btn_inventory '])"

#----- cart page locators -------
check_out_button = (By.ID, "checkout")

# ---- customer information locators -----
first_name_field = (By.ID, "first-name")
last_name_field = (By.ID, "last-name")
zip_code_field = (By.ID, "postal-code")
continue_button = (By.ID, "continue")

# ----- overview page locators ------
finish_button = (By.ID, "finish")


# -------------------------------------------------------

driver = get_driver()
log_in()
add_to_cart_by_product_name()
check_out()
enter_user_information()
print("-- Successfully purchased ---")