from pathlib import Path

from playwright.sync_api import Locator

from autoexercise.pages.base_page import BasePage


class ContactPage(BasePage):
    path = "/contact_us"

    @property
    def heading(self) -> Locator:
        return self.page.locator(".contact-form h2")

    @property
    def success_message(self) -> Locator:
        return self.page.locator(".status.alert-success")

    @property
    def home_button(self) -> Locator:
        return self.page.locator("#form-section").get_by_role("link", name="Home")


    def submit(self, name: str, email: str, subject: str, message: str, file_path: Path) -> None:
        self.page.get_by_test_id("name").fill(name)
        self.page.get_by_test_id("email").fill(email)
        self.page.get_by_test_id("subject").fill(subject)
        self.page.get_by_test_id("message").fill(message)

        self.page.locator("input[name=upload_file]").set_input_files(str(file_path))

        def handle_dialog(dialog):
            print("Dialog appeared:", dialog.message)
            dialog.accept()
            print("Dialog accepted")

        self.page.once("dialog", handle_dialog)
        self.page.locator("input[data-qa='submit-button']").click()
