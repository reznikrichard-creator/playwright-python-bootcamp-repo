import pytest

from autoexercise.data import build_card
from tests.ui.test_cases.steps import (
    add_first_product_from_home,
    delete_account_through_ui,
    sign_up_through_ui,
    verify_address_and_review,
    verify_cart_page_visible,
    verify_home_page_visible,
    verify_logged_in_as,
)

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc15_order_register_before_checkout(app, signup_user):
    # 1-2. Open homepage
    app.home.open()

    # 3. Verify homepage
    verify_home_page_visible(app)

    # 4. Click 'Signup / Login' button
    app.home.nav.login_link.click()

    # 5. Fill all details in Signup and create account
    # 6. Verify 'ACCOUNT CREATED!' and click 'Continue' button
    sign_up_through_ui(app, signup_user)

    # 7. Verify ' Logged in as username' at top
    verify_logged_in_as(app, signup_user["name"])

    # 8. Add products to cart
    add_first_product_from_home(app)
    # 9. Click 'Cart' button
    app.nav.cart_link.click()
    # 10. Verify that cart page is displayed
    verify_cart_page_visible(app)

    # 11. Click Proceed To Checkout
    app.cart.proceed_to_checkout()

    # 12. Verify Address Details and Review Your Order
    verify_address_and_review(app, signup_user, "Blue Top")

    # 13. Enter description in comment text area and click 'Place Order'
    app.checkout.place_order("Please deliver my order carefully.")

    # 14. Enter payment details: Name on Card, Card Number, CVC, Expiration date

    # 15. Click 'Pay and Confirm Order' button
    app.payment.pay(build_card())

    # 16. Verify success message 'Your order has been placed successfully!'
    assert app.order.heading.is_visible()

    # 17. Click 'Delete Account' button
    # 18. Verify 'ACCOUNT DELETED!' and click 'Continue' button
    delete_account_through_ui(app)
