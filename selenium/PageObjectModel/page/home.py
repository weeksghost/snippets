from selenium.webdriver.common.by import By

from base import Base


class HomePage(Base):

    _base_locator = 'q'
    _page_title = u'Google'
    _search_locator = (By.ID, 'lst-ib')
    _title_locator = (By.CSS_SELECTOR, 'h1 > a')

    def __init__(self, testsetup):
        super(HomePage, self).__init__(testsetup)

    def go_to_page(self):
        self.open()

    def search_text(self):
        self.find_element(*self._base_locator)

    def search_box_submit(self):
        search_box = self.find_element(*self._search_locator)
        search_box.submit()


class SearchResultsPage(Base):

    @property
    def title(self):
        pass
