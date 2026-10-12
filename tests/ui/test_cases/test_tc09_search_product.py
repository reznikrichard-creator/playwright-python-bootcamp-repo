# from modulefinder import test
import pytest

from tests.ui.test_cases.steps import verify_home_page_visible, verify_products_page_visible

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc09_search_products(app):
    # 1-2. Open homepage
    app.home.open()

    # 3. Verify homepage
    verify_home_page_visible(app)

    #4. Click on 'Products' button
    app.nav.products_link.click()

    #5. Verify user is navigated to ALL PRODUCTS page successfully & 6. The products list is visible
    verify_products_page_visible(app)

    #6. Enter product name in search input and click search button
    searched_product="Blue Top"
    app.products.search(searched_product)

    #7. Verify 'SEARCHED PRODUCTS' is visible
    app.products.searched_heading.wait_for(state="visible")
    assert app.products.searched_heading.is_visible()

    #8. Verify all the products related to search are visible
    for product in app.products.names.all():
        assert product.is_visible()
        assert searched_product.lower() in product.inner_text().lower()

