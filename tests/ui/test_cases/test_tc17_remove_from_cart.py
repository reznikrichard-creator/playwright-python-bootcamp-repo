import pytest

from tests.ui.test_cases.steps import (
    add_first_product_from_home,
    verify_cart_page_visible,
    verify_home_page_visible,
)

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc17_remove_from_cart(app):
    # 1-2. Open homepage
    app.home.open()

    # 3. Verify homepage
    verify_home_page_visible(app)

    # 4. Add products to cart
    add_first_product_from_home(app)

    #5. Click 'Cart' button
    app.nav.cart_link.click()

    # 6. Verify that cart page is displayed
    verify_cart_page_visible(app)

    # 7. Click 'X' button corresponding to particular product
    app.cart.remove_first_item()

    # 8. Verify that product is removed from the cart
    app.cart.empty_cart.wait_for(state="visible")
    assert app.cart.empty_cart.is_visible()
