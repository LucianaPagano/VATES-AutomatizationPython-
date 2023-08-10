import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.firefox import webdriver
from selenium.webdriver.safari import webdriver
from selenium import webdriver


@pytest.fixture(params={"chrome"})
def driver(request):
    browser = request.param
    print(f"Creating {browser} driver")
    if browser == "chrome":
        driver = webdriver.Chrome()
        yield driver
    elif browser == "safari":
        driver = webdriver.Safari()
        yield driver
        driver.quit()
    print(f"Closing {browser} driver")


