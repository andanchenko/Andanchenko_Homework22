from selenium.webdriver.common.by import By

from page_objects.dashboard_page import DashboardPage
from utilities.web_ui.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __email_input = (By.XPATH, '//input[@id="user-name"]')
    __password_input = (By.CSS_SELECTOR, '#password')
    __login_button = (By.CSS_SELECTOR, '#login-button')

    def set_email(self, email_value):
        self._send_keys(self.__email_input, email_value)
        return self

    def set_password(self, password_value):
        self._send_keys(self.__password_input, password_value)
        return self

    def click_login_button(self):
        self._click(self.__login_button)

    def login(self, email_value, password_value):
        self.set_email(email_value).set_password(password_value).click_login_button()
        return DashboardPage(self._driver)
