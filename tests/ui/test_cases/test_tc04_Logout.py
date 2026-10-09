import re

import pytest

from tests.ui.test_cases.steps import (
    verify_home_page_visible,
    verify_logged_in_as,
)

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc03_Logout(app):
    # 1-2 open the site
    app.home.open()                                         
    verify_home_page_visible(app)
    # 3 click on login link
    assert app.nav.login_link.is_visible()
    app.nav.login_link.click()                              
    # 4 verify login heading
    assert app.login.login_heading.inner_text() == "Login to your account"
    # 5 login with valid credentials
    app.login.login(email = "asdf@asdf", password = "asdf") 
    # 6 verify logged in as
    verify_logged_in_as(app, "asdf")             
    # 7 click on logout link
    app.nav.logout_link.click()                              
    # 8 verify login link is visible and logout link is not visible
    assert app.nav.login_link.is_visible() 
    assert not app.nav.logout_link.is_visible()
    # 9 verify login heading
    assert app.login.login_heading.inner_text() == "Login to your account" 

