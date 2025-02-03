from typing import Literal
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.mark.parametrize("name, expected_name",
                         [("Franklyne", "Franklyne")])
def test_name(name: Literal['Franklyne'], expected_name: Literal['Franklyne']):
    driver = webdriver.Chrome(service=chromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
    driver.find_element(By.XPATH, "//input[@id='user-message']").send_keys(name)
    driver.find_element(By.ID, "showInput").click()
    expected_output = driver.find_element(By.ID, "message").text
    assert expected_output == expected_name, f"Expected {expected_name} but got {expected_output}"
    if expected_output == expected_name:
        print(f"expected output is:  {expected_output}")
    else:
        print("There is an error thith parameterized decorator")