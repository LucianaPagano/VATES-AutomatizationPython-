import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestExceptions:

    @pytest.mark.sin_exceptions
    def test_number1(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # Ponemos tiempo de espera adecuado
        wait = WebDriverWait(driver, 10)
        row_2_input_element = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))

        # Si se llega a esta línea sin generar la excepción, el assert fallará y mostrará el mensaje de error
        assert row_2_input_element.is_displayed()

    @pytest.mark.sin_exceptions
    def test_number2(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # Espera de la carga
        wait = WebDriverWait(driver, 10)
        row_2_input_element = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))

        # Ingreso texto para agregar
        row_2_input_element.send_keys('Apple')

        # Busco el botón "Save" pero de la fila 2
        # save_button = driver.find_element(By.NAME, 'Save')
        # save_button.click()
        driver.find_element(By.XPATH, "(//button[@id='save_btn'])[2]").click()

        # Verifico el texto guardado
        confirmation_element = wait.until(ec.visibility_of_element_located((By.ID, "confirmation")))
        # text_saved = driver.find_element(By.ID, 'confirmation')
        confirmation_message = confirmation_element.text

        assert confirmation_message == "Row 2 was saved"
        driver.quit()

    @pytest.mark.sin_exceptions
    def test_number3(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Edit button
        driver.find_element(By.ID, 'edit_btn').click()

        # Limpio e ingreso el texto
        input_text = driver.find_element(By.XPATH, "//INPUT[@type='text']")
        wait = WebDriverWait(driver, 10)
        wait.until(ec.element_to_be_clickable(input_text))
        input_text.clear()

        # Ingreso banana
        input_text.send_keys('Banana')

        # Click Save
        driver.find_element(By.ID, 'save_btn').click()

        # Verifico
        confirmation_element = wait.until(ec.visibility_of_element_located((By.ID, "confirmation")))
        confirmation_message = confirmation_element.text
        assert confirmation_message == "Row 1 was saved"
        driver.quit()

    @pytest.mark.sin_exceptions
    def test_number4(self, driver):
        # Open Page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Push add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # Find the instructions text element
        wait = WebDriverWait(driver, 10)
        assert wait.until(ec.invisibility_of_element_located((By.ID, "instructions")))

        driver.quit()

    @pytest.mark.sin_exceptions
    def test_number5(self, driver):
        # Open Page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Push add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # Wait for 3 seconds for the second input field to be displayed
        wait = WebDriverWait(driver, 6)
        row_2_input_element = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))

        # Verify second input field is displayed
        assert row_2_input_element.is_displayed(), "Row 2 input should be displayed, but it's not"
        driver.quit()
