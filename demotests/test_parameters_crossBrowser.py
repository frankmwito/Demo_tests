import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@pytest.fixture(params=["chrome", "firefox", "edge"])
def initialize_driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif request.param == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif request.param == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    
    driver.maximize_window() 
    request.cls.driver = driver
    
    print("Browser: ", request.param)
    yield
    
    print("Close Driver")
    driver.quit()
    
@pytest.mark.usefixtures("initialize_driver")
class BaseClass:
    pass

class Test_Drivers(BaseClass):
    def test_multiple_browsers(self):
        self.driver.get("https://www.lambdatest.com/selenium-playground/")
        header = self.driver.find_element(By.XPATH, "//h1[normalize-space()='Selenium Playground']").text
        
        print("Header:", header) 
        assert header == "Selenium Playground", "Test failed"
