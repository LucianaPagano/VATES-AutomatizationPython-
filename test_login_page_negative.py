from PageObjects.loginpage import LoginPage
from PageObjects.test_login_unsuccessfully import LoggedInUnSuccessPAGE
import pytest


class TestNegativeScenarios:
    @pytest.mark.negative
    def test_negative_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login("student", "IncorrectPassword")
        logged_in_page = LoggedInUnSuccessPAGE(driver)
        assert logged_in_page.expected_url == logged_in_page.current_url
        assert logged_in_page.header == "Your password is invalid!"
        assert logged_in_page.is_logout_button_displayed()

