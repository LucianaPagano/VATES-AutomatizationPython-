from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest


class TestPositiveScenarios:
    LOGIN_URL = "https://practicetestautomation.com/practice-test-login"
    LOGGED_IN_URL = "https://practicetestautomation.com/logged-in-successfully/"
    USERNAME = "student"
    PASSWORD = "Password123"

    @pytest.fixture(scope="class")
    def setup_teardown(self) -> webdriver.Chrome:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        yield driver
        driver.quit()

    @pytest.mark.loginpos
    def test_login_positive(self, setup_teardown):
        driver = setup_teardown

        # Go to webpage and fill in the login form
        driver.get(self.LOGIN_URL)
        driver.find_element(By.ID, "username").send_keys(self.USERNAME)
        driver.find_element(By.NAME, "password").send_keys(self.PASSWORD)
        driver.find_element(By.XPATH, "//button[@class='btn']").click()

        # Wait until the new page is loaded and verify the URL
        assert driver.current_url == self.LOGGED_IN_URL

        # Verify the presence of the expected text
        actual_text = driver.find_element(By.TAG_NAME, "h1").text
        assert "Logged In Successfully" in actual_text

        # Verify the presence of the "Log out" button
        assert driver.find_element(By.LINK_TEXT, "Log out").is_displayed()
