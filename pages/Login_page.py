from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    # Locators
    email_address_field = ( By.ID, "input-email")
    password_field = (By.ID, "input-password")
    login_button = (By.XPATH, "//input[@value='Login']")
    warning_message = (By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")