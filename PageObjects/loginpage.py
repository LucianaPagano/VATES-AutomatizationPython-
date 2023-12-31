from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from PageObjects.base_page import BasePage


class LoginPage:
    __url = "https://practicetestautomation.com/practice-test-login/"
    __username_field = (By.ID, "username")
    __password_field = (By.NAME, "password")
    _submit_button = (By.XPATH, "//button[@class=['btn']")

    def __int__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url()
        self._driver.get(self.__url)

    def execute_login(self, username: str, password: str):
        super()._type(self.__username_field, username)
        super()._type(self.__password_field, password)
        super()._click(self._submit_button)