import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import datetime
from datetime import datetime


class TestLambdaTest:
    def test_sample_app_title(self):
        driver = webdriver.Chrome(service=chromeService(ChromeDriverManager().install()))
        driver.get("https://lambdatest.github.io/sample-todo-app/")
        pytest.skip()
        expected_title = "Sample page - lambdatest.com"
        assert expected_title == driver.title
        
    @pytest.mark.skip(reason="Code Has Not Been Deployed")
    def test_ecommerce_title(self):
        driver = webdriver.Chrome(service=chromeService(ChromeDriverManager().insall()))
        driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=product/category&path=17")
        expected_title = "Software"
        assert expected_title == driver.title
        
    @pytest.mark.skipif(
        datetime.now() <= datetime(2099, 12,31),
        reason="Repo is not complete until after finishing tutorial")
    def test_pytest_github_repo(self):
        driver = webdriver.Chrome(service=chromeService(ChromeDriverManager().install()))
        driver.get("https://github.com/RexJones11/PytestTutorials")
        expected_title = "RexJones11"
        print("Title: ", expected_title)
        assert expected_title.__contains__(expected_title)