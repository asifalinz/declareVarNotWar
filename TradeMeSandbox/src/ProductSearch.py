class ProductSearch:

    def __int__(self, page):
        self.page = page
        self._search = page.locator("//input[@id='searchString']")
        self._search_btn = page.locator("//body/div[@id='top-of-page']/div[2]/div[1]/div[2]/div[1]/div[1]/form[1]/div[2]/button[1]")
        self._no_result = page.locator("//div[@id='NoResults']")
        self._search_result = page.locator("//div[contains(text(),'2009, Mazda, Mazda6, WAGON GLX 2.0 M6')]")
        self.description = page.locator("//div[@id='DetailTabs_mainListingDetailTabContentBoxdescription']")

    def enter_search_item(self, s_keyword):
        # clear search field
        self._search.clear()
        # Enter search keyword
        self._search.fill(s_keyword)
        # Search button click
        self._search_btn.click()

    def product_description(self):
        # click on Mazda link
        self._search_result.click()




