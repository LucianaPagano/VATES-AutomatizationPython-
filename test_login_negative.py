import pytest
import time
from selenium.webdriver.common.by import By


class TestNegativeScenarios:
    @pytest.mark.login_negative
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [("incorrectUser", "Password123", "Your username is invalid!"),
                              ("student", "incorrectPassword", "Your password is invalid!")])
    def test_login_negative(self, driver, username, password, expected_error_message):
        # Acceder a la página web
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username "student" into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys(username)

        # Type password "Password123" into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys(password)

        time.sleep(3)

        # Find and click the "Submit" button
        submit_button_locator = driver.find_element(By.ID, "submit")
        submit_button_locator.click()

        time.sleep(3)

        # Verify error message is displayed
        error_message_user = driver.find_element(By.ID, "error")
        assert error_message_user.is_displayed(), "Error message is not displayed, but it should be"

        # Verify error message text is Your username is invalid!
        text_locator = driver.find_element(By.CLASS_NAME, "show")
        actual_text = text_locator.text
        assert actual_text == expected_error_message, "Error message is not expected"

        time.sleep(3)

    # @pytest.mark.login_negative
    # def test_login_negative_psw(self, driver):
    #     # # Ruta al Chromedriver descargado
    #     # chrome_driver_path = 'C:\\Users\\Leito\\Desktop\\WebDriver\\chromedriver.exe'
    #     # # chrome_driver_path = '/ruta/al/chromedriver' # En macOS/Linux
    #     #
    #     # # Configuración del Service de Chrome
    #     # service = ChromeService(executable_path=chrome_driver_path)
    #     #
    #     # # Configuración del controlador Chrome con el Service
    #     # driver = webdriver.Chrome(service=service)
    #     #
    #     # time.sleep(3)
    #
    #     # Acceder a la página web
    #     driver.get("https://practicetestautomation.com/practice-test-login/")
    #
    #     # Type username "student" into Username field
    #     username_locator = driver.find_element(By.ID, "username")
    #     username_locator.send_keys("student")
    #
    #     # Type password "Password123" into Password field
    #     password_locator = driver.find_element(By.NAME, "password")
    #     password_locator.send_keys("IncorrectPassword")
    #
    #     time.sleep(3)
    #
    #     # Find and click the "Submit" button
    #     submit_button_locator = driver.find_element(By.ID, "submit")
    #     submit_button_locator.click()
    #
    #     time.sleep(3)
    #
    #     # Verify error message is displayed
    #     error_message_psw = driver.find_element(By.XPATH, "//div[contains(@id,'error')]")
    #     assert error_message_psw.is_displayed()
    #
    #     # Verify error message text is Your username is invalid!
    #     text_locator = driver.find_element(By.CLASS_NAME, "show")
    #     actual_text = text_locator.text
    #     assert actual_text == "Your password is invalid!"
    #
    #     time.sleep(3)
