from utilities.web_ui.base_page import BasePage
from selenium.webdriver.common.by import By


class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __shopping_card_element = (By.CSS_SELECTOR, "#shopping_cart_container")

    def is_shopping_card_displayed(self):
        return self._is_displayed(self.__shopping_card_element)
