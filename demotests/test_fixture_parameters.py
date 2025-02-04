from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeService
from selenium.webdriver.edge.service import Service as edgeService
from selenium.webdriver.firefox.service import Service as firefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from faker import Faker
import time


@pytest.fixture(autouse=True)
def automatic_fixture():
    print("\nStart of the tests")
    yield
    print("\nEnd of the tests")
    
@pytest.fixture(params=["chrome", "edge", "firefox"])
def driver_initializer(request):
    if request.param == "chrome":
        driver = webdriver.Chrome(service=chromeService(ChromeDriverManager().install()))
    elif request.param == "edge":
        driver = webdriver.Edge(service=edgeService(EdgeChromiumDriverManager().install()))
    elif request.param == "firefox":
        driver = webdriver.Firefox(service=firefoxService(GeckoDriverManager().install()))
    driver.get("https://ecommerce-playground.lambdatest.io/")
    driver.maximize_window()  
    print("Browser:  ",request.param)
    yield driver
    print("Close Driver")
    driver.quit()
    
    
@pytest.mark.usefixtures("driver_initializer")
def test_submit(driver_initializer):
    driver = driver_initializer
    faker = Faker()
    first_name = faker.first_name()  
    last_name = faker.last_name()
    email = faker.email()
    telephone = faker.phone_number()  
    password = faker.password()

    # Hover over My Account
    my_account = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="widget-navbar-217834"]/ul/li[6]/a'))
    )
    actions = ActionChains(driver)
    actions.move_to_element(my_account).perform()

    # Click Register
    register = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Register']"))
    )
    register.click()

    # Fill Registration Form
    driver.find_element(By.ID, "input-firstname").send_keys(first_name)
    driver.find_element(By.ID, "input-lastname").send_keys(last_name)
    driver.find_element(By.ID, "input-email").send_keys(email)
    driver.find_element(By.ID, "input-telephone").send_keys(telephone)
    driver.find_element(By.ID, "input-password").send_keys(password)
    driver.find_element(By.ID, "input-confirm").send_keys(password)

    # Click radio buttons
    driver.find_element(By.XPATH, "//label[normalize-space()='No']").click()
    driver.find_element(By.XPATH, "//label[normalize-space()='Yes']").click()

    # Click agree checkbox
    agree_checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//label[@for='input-agree']"))
    )
    agree_checkbox.click()

    # Click continue
    continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@value='Continue']"))
    )
    continue_button.click()

    # Wait for success page
    time.sleep(2)
    assert "success" in driver.current_url or "account/success" in driver.current_url, "Registration was not successful."
