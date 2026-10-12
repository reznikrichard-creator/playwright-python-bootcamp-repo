import pytest

from tests.ui.test_cases.steps import verify_home_page_visible

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc12_add_products_to_cart(app):
    # 1-2. Open homepage
    app.home.open()

    # 3. Verify homepage
    verify_home_page_visible(app)

    #4. Click on 'Products' button
    app.nav.products_link.click()

    #5. Hover over first product and click 'Add to cart' & 6. Click 'Continue Shopping' button
    app.products.add_to_cart(0)

    #7. Hover over second product and click 'Add to cart'
    app.products.add_to_cart(1, continue_shopping= False)

    #8. Click 'View Cart' button
    app.products.view_cart_from_modal()

    # 9. Verify both products are added to Cart
    assert app.cart.product_rows.count() == 2

    first = app.cart.product_rows.nth(0)
    second = app.cart.product_rows.nth(1)

    assert first.get_by_text("Blue Top").is_visible()
    assert second.get_by_text("Men Tshirt").is_visible()

    # 10. Verify their prices, quantity and total price

    # First product - Blue Top
    assert app.cart.unit_prices.nth(0).inner_text() == "Rs. 500"
    assert app.cart.quantities.nth(0).inner_text() == "1"
    assert app.cart.totals.nth(0).inner_text() == "Rs. 500"

    # Second product - Men Tshirt
    assert app.cart.unit_prices.nth(1).inner_text() == "Rs. 400"
    assert app.cart.quantities.nth(1).inner_text() == "1"
    assert app.cart.totals.nth(1).inner_text() == "Rs. 400"