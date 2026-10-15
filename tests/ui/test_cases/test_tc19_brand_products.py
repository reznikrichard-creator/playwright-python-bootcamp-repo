import pytest

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc19_brand_products(app):
    # 1-2. Open homepage
    app.home.open()

    # 3. Click on 'Products' button
    app.nav.products_link.click()

    # 4. Verify that Brands are visible on left side bar
    assert app.products.sidebar.brands_heading.is_visible()

    # 5. Click on any brand name
    app.sidebar.open_brand("Polo")

    # 6. Verify that user is navigated to brand page and brand products are displayed
    app.category.verify_brand("Polo")
    # 7. On left side bar, click on any other brand link
    app.sidebar.open_brand("H&M")
    # 8. Verify that user is navigated to that brand page and can see products
    app.category.verify_brand("H&M")