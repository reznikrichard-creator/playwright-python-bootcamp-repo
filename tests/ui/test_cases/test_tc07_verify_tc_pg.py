from modulefinder import test
import pytest

from autoexercise.data import SAMPLE_FILE
from autoexercise.pages import contact_page, test_cases_page
from tests.ui.test_cases.steps import (
    verify_home_page_visible
)

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc07_verify_tc_pg(app):
    # 1-2. Open homepage
    app.home.open()

    # 3. Verify homepage
    verify_home_page_visible(app)

    # 4. Click Test Cases
    app.nav.test_cases_link.click()

    # 5. Verify Test Cases page
    assert app.test_cases.heading.is_visible()
