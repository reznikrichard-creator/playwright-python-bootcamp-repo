from playwright.sync_api import Locator

from autoexercise.pages.products_page import ProductsPage


class CategoryPage(ProductsPage):

    @property
    def heading(self) -> Locator:
        return self.page.locator(".features_items h2.title")

    def verify_category(self, category: str, subcategory: str) -> None:
        expected = f"{category} - {subcategory} PRODUCTS"

        self.heading.wait_for(state="visible")
        assert self.heading.inner_text().strip().upper() == expected.upper()
        assert self.cards.count() > 0

    def verify_brand(self, brand: str) -> None:
        expected = f"BRAND - {brand} PRODUCTS"

        self.heading.wait_for(state="visible")
        assert self.heading.inner_text().strip().upper() == expected.upper()
        assert self.cards.count() > 0