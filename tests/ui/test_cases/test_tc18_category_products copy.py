import pytest

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc18_category_products(app):
    # 1-2. Open homepage
    app.home.open()

    # 3. Verify that categories are visible on left side bar
    assert app.home.sidebar.categories_heading.is_visible()

    # 4. Click on 'Women' category
    app.home.sidebar.open_category("Women")

    # 5. Click on any category link under 'Women' category, for example: Dress
    app.home.sidebar.open_subcategory("Women", "Dress")
    # 6. Verify that category page is displayed and confirm text 'WOMEN - TOPS PRODUCTS'
    app.category.heading.wait_for(state="visible")
    assert app.category.heading.inner_text().lower() == "women - dress products"
    # 7. Click Men category
    app.sidebar.open_category("Men")

    # 8. Click Tshirts
    app.sidebar.open_subcategory("Men", "Tshirts")

    # 9. Verify Men category page
    app.category.heading.wait_for(state="visible")
    assert app.category.heading.inner_text().lower() == "men - tshirts products"