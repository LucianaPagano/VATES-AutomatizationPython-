from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from PageObjects.base_page import BasePage

class LoggedInSuccessPAGE(BasePage):
    __actual_url = "https://practicetestautomation.com/practice-test-login/"
    __header_locator = (By.TAG_NAME, "h1")
    __log_out_button_locator = (By.LINK_TEXT, "Log out")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def header(self) -> str:
        return self._driver.find_element(self.__header_locator).text

    @property
    def current_url(self) -> str:
        return self

    def is_logout_button_displayed(self) -> bool:
        return self._driver.find_element(self.__log_out_button_locator).is_displayed()
