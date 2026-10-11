import pytest

from autoexercise.data import SAMPLE_FILE
from autoexercise.pages import contact_page
from tests.ui.test_cases.steps import (
    verify_home_page_visible
)

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc06_Contact_us(app):
    # 1. Launch browser 2. Navigate to url 'http://automationexercise.com'
    app.home.open()                      

    #3. Verify that home page is visible successfully                   
    verify_home_page_visible(app)

    #4. Click on 'Contact Us' button
    app.nav.contact_link.click()

    #5. Verify 'GET IN TOUCH' is visible
    assert app.contact.heading.inner_text() ==  "Get In Touch"

    #6. Enter name, email, subject and message          | 7. Upload file |   8. Click 'Submit' button
    app.contact.submit("Rich","rez@rez.com", "hello", "hello", file_path=SAMPLE_FILE)

    #10. Verify success message 'Success! Your details have been submitted successfully.' is visible
    app.contact.success_message.wait_for(state="visible", timeout=20000)

    assert app.contact.success_message.inner_text() == \
    "Success! Your details have been submitted successfully."

    #11. Click 'Home' button and verify that landed to home page successfully
    app.contact.home_button.click()
    verify_home_page_visible(app)