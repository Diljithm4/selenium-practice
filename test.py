from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from datetime import date

def setup_driver():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    return webdriver.Chrome(service=service, options=options)

def wait_for_element(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))

with setup_driver() as driver:
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    # Fill Form Fields
    wait_for_element(driver, By.NAME, "my-text").send_keys("Hello, Selenium!")
    wait_for_element(driver, By.NAME, "my-password").send_keys("password")
    wait_for_element(driver, By.NAME, "my-textarea").send_keys("Hello World !!")
    
    # Dropdown & Data List Selection
    wait_for_element(driver, By.NAME, "my-select").send_keys("One")
    wait_for_element(driver, By.NAME, "my-datalist").send_keys("New York")

    # File Upload
    file_path = r"C:\Users\dilji\Downloads\Documents\file_test.pdf"
    wait_for_element(driver, By.NAME, "my-file").send_keys(file_path)

    # Checkbox Handling
    def toggle_checkbox(element, should_check=True):
        if element.is_selected() != should_check:
            element.click()

    toggle_checkbox(wait_for_element(driver, By.ID, "my-check-1"), False)
    toggle_checkbox(wait_for_element(driver, By.ID, "my-check-2"), True)

    # Radio Button Handling
    def select_radio_button(element):
        if not element.is_selected():
            element.click()

    select_radio_button(wait_for_element(driver, By.ID, "my-radio-2"))

    # Color Picker
    wait_for_element(driver, By.NAME, "my-colors").send_keys("#000000")

    # Date Picker (Fixed Format)
    date_picker = wait_for_element(driver, By.NAME, "my-date")
    driver.execute_script("arguments[0].value = arguments[1];", date_picker, date.today().strftime("%Y-%m-%d"))

    # Range Slider
    range_picker = wait_for_element(driver, By.NAME, "my-range")
    driver.execute_script("arguments[0].value = 0;", range_picker)
    driver.execute_script("arguments[0].dispatchEvent(new Event('input'))", range_picker)

    # Click Submit
    wait_for_element(driver, By.CLASS_NAME, "btn").click()

    # Validate Submission
    WebDriverWait(driver, 5).until(EC.url_changes(driver.current_url))

    input("Press Enter to close the browser...")
