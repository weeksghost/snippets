from element import BasePageElement
from locators import MainPageLocators, SearchResultsPageLocators


class SearchTextElement(BasePageElement):

    locator = 'q'


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    search_text_element = SearchTextElement()

    def is_title_matches(self):
        return 'Google' in self.driver.title

    def click_submit(self):
        element = self.driver.find_element(*MainPageLocators.SUBMIT)
        element.submit()


class SearchResultsPage(BasePage):

    def is_results_found(self):
        # Non-specific search acceptance criteria
        return 'No results found.' not in self.driver.page_source
