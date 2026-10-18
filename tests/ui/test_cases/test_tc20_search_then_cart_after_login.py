import pytest

from tests.ui.test_cases.steps import verify_home_page_visible, verify_products_page_visible

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc20_search_then_cart_after_login(app):
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    app.home.open()
    # 3. Click on 'Products' button
    app.nav.products_link.click()
    # 4. Verify user is navigated to ALL PRODUCTS page successfully
    verify_products_page_visible(app)
    # 5. Enter product name in search input and click search button
    searched_product="Blue Top"
    app.products.search(searched_product)
    # 6. Verify 'SEARCHED PRODUCTS' is visible
    app.products.searched_heading.wait_for(state="visible")
    assert app.products.searched_heading.is_visible()

    # 7. Verify all the products related to search are visible
    for product in app.products.names.all():
        assert product.is_visible()
        assert searched_product.lower() in product.inner_text().lower()
    # 8. Add those products to cart
    # 9. Click 'Cart' button and verify that products are visible in cart
    # 10. Click 'Signup / Login' button and submit login details
    # 11. Again, go to Cart page
    # 12. Verify that those products are visible in cart after login as well
