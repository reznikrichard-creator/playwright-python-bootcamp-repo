#Paramertize 14 15 16

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

@pytest.mark.parametrize(
    "scenario",
    [
        "register_during_checkout",
        "register_before_checkout",
        "login_before_checkout"
    ]
)


def test_checkout_scenerios(app, scenario):

    user = build_user()

    if scenario == "login_before_checkout":
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


    if scenario == "register_before_checkout":
        #4. Click 'Signup / Login' button
        app.home.nav.login_link.click()

        # 5. Fill all details in Signup and create account
        # 6. Verify 'ACCOUNT CREATED!' and click 'Continue' button
        sign_up_through_ui(app, user)

        # 7. Verify ' Logged in as username' at top
        verify_logged_in_as(app, user["name"])

    if scenario == "login_before_checkout":
        # Click 'Signup / Login' button
        app.home.nav.login_link.click()
        # Fill email, password and click 'Login' button
        app.login.login(user["email"], user["password"])
        #  Verify 'Logged in as username' at top
        verify_logged_in_as(app, user["name"])

    # 4. Add products to cart
    add_first_product_from_home(app)

    #5. Click 'Cart' button
    app.nav.cart_link.click()

    # 6. Verify that cart page is displayed
    verify_cart_page_visible(app)

    #7. Click Proceed To Checkout
    app.cart.proceed_to_checkout()

    if scenario == "register_during_checkout":
        # Click 'Register / Login' button
        app.cart.register_login_link.click()

        # Fill all details in Signup and create account 
        # 10. Verify 'ACCOUNT CREATED!' and click 'Continue' button
        sign_up_through_ui(app, user)

        # Verify ' Logged in as username' at top
        verify_logged_in_as(app, user["name"])

        # Click 'Cart' button and verify result
        app.home.nav.cart_link.click()
        verify_cart_page_visible(app)

        # Click 'Proceed To Checkout' button
        app.cart.proceed_to_checkout()

    # 14. Verify Address Details and Review Your Order
    verify_address_and_review(app, user, "Blue Top")

    # 15. Enter description in comment text area and click 'Place Order'
    app.checkout.place_order("Please deliver my order carefully.")

    # 16. Enter payment details: Name on Card, Card Number, CVC, Expiration date
    # 17. Click 'Pay and Confirm Order' button
    app.payment.pay(build_card())

    # 18. Verify success message 'Your order has been placed successfully!'
    assert app.order.heading.is_visible()
    
    # 19. Click 'Delete Account' button
    # 20. Verify 'ACCOUNT DELETED!' and click 'Continue' button
    delete_account_through_ui(app)