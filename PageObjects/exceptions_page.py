from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from PageObjects.base_page import BasePage
import pytest

class ExceptionsPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-exceptions/"
    __add_button_locator = (By.ID, "add_btn")
    row_2_input_element = (By.XPATH, "//div[@id='row2']/input")
    row_2_input_element.send_keys("Sushi")
    row_2_save_button = (By.XPATH, "//div[@id='row2']/input")
    __confirmation_element =
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self._driver = driver

    def open(self):
        super()._open_url(self.__url)

    def add_second_row(self):
        super()._click(self.__add_button_locator)
        super()._wait_until_element_is_visible(self.row_2_input_element, WebDriver)

    def is_row2_displayed(self) -> bool:
        return super()._is_displayed(self.row_2_input_element)

    def add_second_row(self):
        super()._click(self.__add_button_locator)
        super()._wait_until_element_is_visible(self.row_2_input_element)

    def add_second_food(self, food:str) -> str:
        super()._type(self.row_2_input_element, food)
        super()._click(self.row_2_input_element)
        super()._wait_until_element_is_visible(self.__confirmation_element)

    def get_confirmation_message(self) -> str:
        return super().get_text(self.__confirmation_element)
