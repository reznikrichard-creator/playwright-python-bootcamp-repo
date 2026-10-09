import pytest

from tests.ui.test_cases.steps import (
    verify_home_page_visible,
    verify_logged_in_as,
)

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc02_Login_Happy_Path(app):
    # 1-2 Open the application website
    app.home.open()

    # 3 Verify the home page is displayed successfully
    verify_home_page_visible(app)

    # 4 Click the Login link in the navigation menu
    assert app.nav.login_link.is_visible()
    app.nav.login_link.click()

    # 5 Verify the login page displays the correct heading
    assert app.login.login_heading.inner_text() == "Login to your account"

    # 6-7 Enter valid email and password, then click Login
    app.login.login(email="asdf@asdf", password="asdf")

    # 8 Verify the user is successfully logged in with the correct username
    verify_logged_in_as(app, "asdf")

def test_tc03_Login_Unhappy_Path(app):
    # 1-2 Open the application website
    app.home.open()

    # 3 Verify the home page is displayed successfully
    verify_home_page_visible(app)

    # 4 Verify the Login link is visible, then click it
    assert app.nav.login_link.is_visible()
    app.nav.login_link.click()

    # 5 Verify the login page displays the correct heading
    assert app.login.login_heading.inner_text() == "Login to your account"

    # 6-7 Enter a valid email with an invalid password, then click Login
    app.login.login(email="asdf@asdf", password="asf")

    # 8 Verify the expected error message is displayed
    assert app.login.error_message.inner_text() == "Your email or password is incorrect!"