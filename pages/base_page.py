

from selenium.webdriver.common.by import By

class BasePage:
    # The purpose of a BasePage is to contain methods common to all page objects
    def __init__(self, driver):
        self.driver = driver
        
    def find(self, *locator):
        return self.driver.find_element(*locator)
    # the asterick before the locator argument allows the function to accept only keyword arguments
    
    def click(self, *locator):
        self.find(*locator).click()
        # self.driver.find_element(*locator).click()
        
    def set(self, locator, value):
        self.find(*locator).clear()
        self.find(*locator).send_keys(value)
        
    def get_text(self, locator):
        return self.find(*locator).text
    
    def get_title(self):
        return self.driver.title
    
    def click_right_menu_page(self, page_name):
        #self.click(self.page(page_name)) # calling the page method to get the Locator of the page
        page = By.XPATH, f"//aside[@id='column-right']//a[text()=' "+ page_name +"']"
        self.click(page)
        
    # Below method allows us to click page, check if page is visible, & More Actions 
    def page(self, page_name):
        return By.XPATH, f"//aside[@id='column-right']//a[text()=' "+ page_name +"']"