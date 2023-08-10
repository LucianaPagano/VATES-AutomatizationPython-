
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestExceptions:

    @pytest.mark.exceptions
    def test_number1(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # Intentar encontrar el campo de entrada de la fila 2 sin usar tiempo de espera adecuado
        row_2_input_element = driver.find_element(By.XPATH, "//div[@id='row2']/input")

        # Si se llega a esta línea sin generar la excepción, el assert fallará y mostrará el mensaje de error
        assert row_2_input_element.is_displayed()

    @pytest.mark.exceptions
    def test_number2(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        # Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()
        wait = WebDriverWait(driver, 10)
        row_2_input_element = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))
        # Verify Row 2 input field is displayed
        assert row_2_input_element.is_displayed(), "Row 2 input should be displayed, but it's not"
        #
        row_2_input_element.send_keys('text')
        save_button = driver.find_element(By.NAME, 'Save')
        save_button.click()

        text_saved = driver.find_element(By.ID, 'confirmation')

        assert text_saved.is_displayed()
        driver.quit()

    @pytest.mark.exceptions
    def test_number3(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        # Click Add button
        # edit_button = driver.find_element(By.ID,'edit_btn')
        # edit_button.click()

        input_text = driver.find_element(By.XPATH, "//INPUT[@type='text']")
        input_text.clear()
        input_text.send_keys('text')

        save_btn = driver.find_element(By.ID, 'save_btn')
        save_btn.click()
        driver.quit()

    @pytest.mark.exceptions
    def test_number4(self, driver):
        # Open Page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Find the instructions text element
        instruction_text = driver.find_element(By.ID, "instructions")
        assert instruction_text.is_displayed()

        # Push add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # Verify instruction text element is no longer displayed
        assert instruction_text.is_displayed()
        driver.quit()

    @pytest.mark.exceptions
    def test_number5(self, driver):
        # Open Page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Push add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # Wait for 3 seconds for the second input field to be displayed
        wait = WebDriverWait(driver, 3)
        row_2_input_element = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))

        # Verify second input field is displayed
        assert row_2_input_element.is_displayed(), "Row 2 input should be displayed, but it's not"
        driver.quit()
