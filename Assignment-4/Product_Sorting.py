import tempfile
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
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


def get_price_list():
    price_list = []
    price_element = wait.until(EC.visibility_of_all_elements_located(inventory_item_price))
    for price in price_element:
        temp = price.text
        temp = temp.replace("$","")
        price_list.append(temp)
    return price_list

def validate_price_high_to_low():
    price_list = get_price_list()
    print("price(high-low): ", price_list)
    flag = True  # assume the price list is in high to low order
    for i in range(len(price_list)-1):
        if float(price_list[i]) >= float(price_list[i+1]):
            continue
        else:
            flag = False
            break

    assert flag == True, "Products price are not in high to low order"

def validate_price_low_to_high():
    price_list = get_price_list()
    print("price(low-high): ", price_list)
    flag = True  # assume the price list is in high to low order
    for i in range(len(price_list) - 1):
        if float(price_list[i]) <= float(price_list[i+1]):
            continue
        else:
            flag = False
            break

    assert flag == True, "Products price are not in low to high order"

def get_products_name():
    products_name = []
    name_elements = wait.until(EC.visibility_of_all_elements_located(inventory_item_name))
    for name in name_elements:
        products_name.append(name.text)

    return products_name

def validate_product_sort_A_to_Z():
    product_name = get_products_name()
    print("Name(A-Z): ", product_name)
    flag = True  # assuming that products are sorted in a to z
    for i in range(len(product_name)-1):
        if product_name[i].lower() <= product_name[i+1].lower():
            continue
        else:
            flag = False
            break

    assert flag == True, "Products are not sorted in A to Z"

def validate_product_sort_Z_to_A():
    product_name = get_products_name()
    print("Name(Z-A): ",product_name)
    flag = True  # assuming that products are sorted in a to z
    for i in range(len(product_name) - 1):
        if product_name[i].lower() >= product_name[i + 1].lower():
            continue
        else:
            flag = False
            break

    assert flag == True, "Products are not sorted in Z to A"

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
product_sort_locator = (By.CLASS_NAME, "product_sort_container")
inventory_item_price = (By.XPATH, "//div[@class='inventory_item_price']")

# -------------------------------------------------------

driver = get_driver()
wait = WebDriverWait(driver,10)

log_in()

dropdown_element = wait.until(EC.visibility_of_element_located(product_sort_locator))
select = Select(dropdown_element)
select.select_by_visible_text("Price (high to low)")
validate_price_high_to_low()

dropdown_element = wait.until(EC.visibility_of_element_located(product_sort_locator))
select = Select(dropdown_element)
select.select_by_visible_text("Price (low to high)")
validate_price_low_to_high()

dropdown_element = wait.until(EC.visibility_of_element_located(product_sort_locator))
select = Select(dropdown_element)
select.select_by_index(0)  # A to Z
validate_product_sort_A_to_Z()

dropdown_element = wait.until(EC.visibility_of_element_located(product_sort_locator))
select = Select(dropdown_element)
select.select_by_value("za")  # Z to A
validate_product_sort_Z_to_A()

print("--- All types of sort validated ---")
