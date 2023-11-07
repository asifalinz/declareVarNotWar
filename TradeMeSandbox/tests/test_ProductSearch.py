from playwright.sync_api import Page, expect
from TradeMeSandbox.src.LandingPage import LandingPage
from TradeMeSandbox.src.ProductSearch import ProductSearch


def test_product_search(set_up_tear_down) -> None:
    page = set_up_tear_down
    keyword = "mazda"
    p_search = ProductSearch()
    p_search.enter_search_item(keyword)
    p_search.product_description()
    expect(p_search.description).to_be_visible()
    expect(p_search.description).to_have_text("mazda")
