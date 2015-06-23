from selenium.webdriver.common.by import By

from base import Base
from page import PageRegion


class HomePage(Base):

    _search_text_element = 'q'
    _page_title = u'Google'
    _search_locator = (By.ID, 'lst-ib')
    _title_locator = (By.CSS_SELECTOR, 'h1 > a')

    def __init__(self, testsetup):
        super(HomePage, self).__init__(testsetup)

    def go_to_page(self):
        self.open()


    def click_submit(self):
        element = self.find_element(*self._search_locator)
        return element


class SearchResultsPage(PageRegion):

    @property
    def title(self):
        # Non-specific search acceptance criteria
        return 'No results found.' not in self.driver.page_source
