import pytest

from autoexercise.data import build_card, build_user
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


def test_tc16_order_login_before_checkout(app):
    user = build_user()

    # SETUP 
    # Register a new user
    app.home.open()

    # Navigate to Signup/Login page
    app.home.nav.login_link.click()

    # Register new account
    sign_up_through_ui(app, user)

    # Log out after registration
    app.nav.logout_link.click()

    # 1-2. Open homepage
    app.home.open()

    # 3. Verify homepage
    verify_home_page_visible(app)

    # 4. Click 'Signup / Login' button
    app.home.nav.login_link.click()
    # 5. Fill email, password and click 'Login' button
    app.login.login(user["email"], user["password"])
    # 6. Verify 'Logged in as username' at top
    verify_logged_in_as(app, user["name"])
    # 7. Add products to cart
    add_first_product_from_home(app)
    # 8. Click 'Cart' button
    app.nav.cart_link.click()
    # 9. Verify that cart page is displayed
    verify_cart_page_visible(app)
    # 10. Click Proceed To Checkout
    app.cart.proceed_to_checkout()
    # 11. Verify Address Details and Review Your Order
    verify_address_and_review(app, user, "Blue Top")
    # 12. Enter description in comment text area and click 'Place Order'
    app.checkout.place_order("Please deliver my order carefully.")
    # 13. Enter payment details: Name on Card, Card Number, CVC, Expiration date
    # 14. Click 'Pay and Confirm Order' button
    app.payment.pay(build_card())
    # 15. Verify success message 'Your order has been placed successfully!'
    assert app.order.heading.is_visible()
    # 16. Click 'Delete Account' button
    # 17. Verify 'ACCOUNT DELETED!' and click 'Continue' button
    delete_account_through_ui(app)



