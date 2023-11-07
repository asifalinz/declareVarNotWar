from playwright.sync_api import Page, expect
from TradeMeSandbox.src.LandingPage import LandingPage


def test_landing_page(set_up_tear_down) -> None:
    page = set_up_tear_down
    landing_p = LandingPage()
    expect(landing_p.verify_title).to_be_visible()


def test_product_search(page: Page) -> None:
    page.goto("https://www.tmsandbox.co.nz/")

