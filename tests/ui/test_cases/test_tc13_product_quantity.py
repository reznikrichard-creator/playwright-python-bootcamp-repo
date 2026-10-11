import pytest

from autoexercise.pages import cart_page, base_page, products_page
from tests.ui.test_cases.steps import (
    verify_home_page_visible,
    verify_products_page_visible
)

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc13_product_quantity(app):
    # 1-2. Open homepage
    app.home.open()

    # 3. Verify homepage
    verify_home_page_visible(app)
    # 4. Click 'View Product' for any product on home page

    # 5. Verify product detail is opened

    # 6. Increase quantity to 4

    # 7. Click 'Add to cart' button

    # 8. Click 'View Cart' button
    
    # 9. Verify that product is displayed in cart page with exact quantity
