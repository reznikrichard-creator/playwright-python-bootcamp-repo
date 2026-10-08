import re

import pytest

from tests.ui.test_cases.steps import (
    delete_account_through_ui,
    verify_home_page_visible,
    verify_logged_in_as,
)

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc03_Logout(app):
    app.home.open()                                         
    verify_home_page_visible(app)                         
    app.nav.login_link.click()                             
    assert app.nav.login_link.is_visible()  
    assert app.login.login_heading.inner_text() == "Login to your account"
    app.login.login(email = "asdf@asdf", password = "asdf") 
    verify_logged_in_as(app, "asdf")             
    app.nav.logout_link.click()                              
    assert app.nav.login_link.is_visible() 
    assert app.login.login_heading.inner_text() == "Login to your account" 

