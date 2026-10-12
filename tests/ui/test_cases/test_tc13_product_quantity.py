import pytest

from tests.ui.test_cases.steps import verify_home_page_visible, verify_products_details_page_visible

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc13_product_quantity(app):
    # 1-2. Open homepage
    app.home.open()
    # 3. Verify homepage
    verify_home_page_visible(app)
    # 4. Click 'View Product' for any product on home page
    app.products.open_product_details(app.products.cards.first)
    # 5. Verify product detail is opened
    verify_products_details_page_visible(app)
    # 6. Increase quantity to 4
    app.product_detail.set_quantity("4")
    # 7. Click 'Add to cart' button
    app.product_detail.add_to_cart()
    # 8. Click 'View Cart' button
    app.product_detail.view_cart_from_modal()
    # 9. Verify that product is displayed in cart page with exact quantity
    first = app.cart.rows.nth(0)

    assert first.get_by_text("Blue Top").is_visible()

    assert app.cart.quantities.nth(0).inner_text() == "4"
