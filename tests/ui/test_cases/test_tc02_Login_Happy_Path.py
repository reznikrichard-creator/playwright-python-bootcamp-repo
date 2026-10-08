import re

import pytest

from tests.ui.test_cases.steps import (
    delete_account_through_ui,
    verify_home_page_visible,
    verify_logged_in_as,
)

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc02_Login_Happy_Path(app, login_page):
    app.home.open()                                           # 1-2 open the site
    verify_home_page_visible(app)                             # 3
    app.nav.login_link.click()                                # 4
    assert app.login.login_heading.inner_text() == "Login to your account"  # 5
    app.login.login(email = "asdf@asdf", password = "asdf")  # 6-7 
    verify_logged_in_as(app, "asdf")             # 8

def test_tc03_Login_Unhappy_Path(app, login_page):
    app.home.open()                                           # 1-2 open the site
    verify_home_page_visible(app)                             # 3
    app.nav.login_link.click()                                # 4
    assert app.login.login_heading.inner_text() == "Login to your account"  # 5
    app.login.login(email = "asdf@asdf", password = "asf")  # 6-7 
    assert app.login.error_message.inner_text() == "Your email or password is incorrect!"  # 8