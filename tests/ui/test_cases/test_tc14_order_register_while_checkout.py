import pytest

from autoexercise.data import build_card
from autoexercise.pages import checkout_page


from tests.ui.test_cases.steps import delete_account_through_ui, verify_address_and_review, verify_logged_in_as, verify_home_page_visible,add_first_product_from_home,verify_cart_page_visible,  sign_up_through_ui

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc14_order_register_while_checkout(app, signup_user):
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

    #7. Click Proceed To Checkout
    app.cart.proceed_to_checkout()

    # 8. Click 'Register / Login' button
    app.cart.register_login_link.click()

    # 9. Fill all details in Signup and create account # 10. Verify 'ACCOUNT CREATED!' and click 'Continue' button
    sign_up_through_ui(app, signup_user)

    # 11. Verify ' Logged in as username' at top
    verify_logged_in_as(app, signup_user["name"])

    # 12.Click 'Cart' button
    app.home.nav.cart_link.click()

    # 13. Click 'Proceed To Checkout' button
    app.cart.proceed_to_checkout()

    # 14. Verify Address Details and Review Your Order
    verify_address_and_review(app, signup_user, "Blue Top")

    # 15. Enter description in comment text area and click 'Place Order'
    app.checkout.place_order("Please deliver my order carefully.")
    # 16. Enter payment details: Name on Card, Card Number, CVC, Expiration date
    app.payment.pay(build_card())
    # 17. Click 'Pay and Confirm Order' button
    
    # 18. Verify success message 'Your order has been placed successfully!'
    assert app.order.heading.is_visible()
    # 19. Click 'Delete Account' button
    delete_account_through_ui(app)
    # 20. Verify 'ACCOUNT DELETED!' and click 'Continue' button


