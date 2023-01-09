import pytest

from utilities.config_parser import ReadConfig


@pytest.mark.first_test
def test_01(open_login_page):
    login_page = open_login_page
    user_data = ReadConfig.get_password()
    user_name = user_data[0]
    password = user_data[1]
    dashboard_page = login_page.login(user_name, password)
    assert dashboard_page.is_shopping_card_displayed() is True, 'User was not logged-in'
