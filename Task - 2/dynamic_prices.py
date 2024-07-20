from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def extract_discount_price(url, item_selector, add_to_cart_selector, discount_price_selector):
    # Setup WebDriver using ChromeDriverManager
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Open the webpage
        driver.get(url)

        # Wait for the item to be present and click on it
        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, item_selector))
        ).click()

        # Wait for the add to cart button to be present and click on it
        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, add_to_cart_selector))
        ).click()

        # Wait for the discount price to appear (e.g., in the cart or a popup)
        discount_price_element = WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, discount_price_selector))
        )

        # Extract and print the discount price
        discount_price = discount_price_element.text
        print(f"Discount Price: {discount_price}")

    finally:
        # Close the browser
        driver.quit()

# Replace the CSS selectors and URL with the actual ones
url = 'https://www.flipkart.com'
item_selector = '.item-class'  # CSS selector for the item
add_to_cart_selector = '.add-to-cart-button-class'  # CSS selector for the add to cart button
discount_price_selector = '.discount-price-class'  # CSS selector for the discount price

extract_discount_price(url, item_selector, add_to_cart_selector, discount_price_selector)
