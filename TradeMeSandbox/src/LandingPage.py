
class LandingPage:
    def __int__(self, page):
        self.page = page
        self.title = page.locator("//img[@id='SiteHeader_SiteTabs_kevin']")

    @property
    def verify_title(self):
        return self.title
        #expect(trade_me).to_be_visible()
