import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest


class TestPositiveScenarios:
    LOGIN_URL = "https://practicetestautomation.com/practice-test-login"
    LOGGED_IN_URL = "https://practicetestautomation.com/logged-in-successfully/"
    USERNAME = "student"
    PASSWORD = "incorrectPassword"

    @pytest.fixture(scope="class")
    def setup_teardown(self) -> webdriver.Chrome:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        yield driver
        driver.quit()

    @pytest.mark.Login_neg
    def test_login_negative(self, setup_teardown):
        driver = setup_teardown

        # Go to webpage and fill in the login form
        driver.get(self.LOGIN_URL)
        driver.find_element(By.ID, "username").send_keys(self.USERNAME)
        driver.find_element(By.NAME, "password").send_keys(self.PASSWORD)
        driver.find_element(By.XPATH, "//button[@class='btn']").click()

        error_message_user = driver.find_element(By.ID, "Error")
        assert error_message_user.is_displayed()

        text_locator = driver.find_element(By.CLASS_NAME, "show")
        actual_text = text_locator
        assert "Your password is invalid!" in actual_text

        time.sleep(20)