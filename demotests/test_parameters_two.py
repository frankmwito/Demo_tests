from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import math

@pytest.mark.parametrize("num1, num2, expected_total",
                         [("25", "25", "50"),
                          ("10", "10", "20"),
                          ("30", "40", "70")])


def test_lambdaest_two_input_fields(num1, num2, expected_total):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
    driver.find_element(By.ID, "sum1").send_keys(num1)
    driver.find_element(By.ID, "sum2").send_keys(num2)
    driver.find_element(By.XPATH, "//button[normalize-space()='Get Sum']").click()
    result = driver.find_element(By.ID, "addmessage").text
    
    assert expected_total == result, "Wrong answer"
    
    
@pytest.mark.parametrize("base", [1,  2, 3])
@pytest.mark.parametrize("exponent", [4,  5, 6])

def test_raising_base_to_power(base, exponent):
    result = base ** exponent
    assert result == math.pow(base, exponent)