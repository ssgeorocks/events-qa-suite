import pytest
from framework.pages.login_page import LoginPage
from framework.pages.profile_page import ProfilePage


@pytest.mark.e2e
def test_login_from_browser(driver, settings, registered_user):

    login_page = LoginPage(driver, settings.base_url)
    profile_page = ProfilePage(driver)

    login_page.open()
    login_page.login(registered_user["email"], registered_user["password"])
    profile_page.wait_for_page()
    assert profile_page.email == registered_user["email"]

