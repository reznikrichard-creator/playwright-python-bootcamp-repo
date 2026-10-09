import pytest

from tests.ui.test_cases.steps import (
    verify_home_page_visible,
)

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc04_register_w_existing_email(app):
    app.home.open()                                           # 1-2 open the site
    verify_home_page_visible(app)                             # 3
    app.nav.login_link.click()                                # 4
    assert app.login.signup_heading.inner_text() == "New User Signup!"  # 5
    app.login.start_signup("Richard", "asdf@asdf.com")  # 6-7
    assert app.login.email_already_exists_error_message.is_visible()  # 8
    assert not app.nav.logged_in_as.is_visible() # 9
