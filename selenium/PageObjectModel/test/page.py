from element import BasePageElement
from locators import MainPageLocators, SearchResultsPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class BasePage(object):
    '''Base page object'''

    implicit_wait = 10

    def __init__(self, resource_handler):
        self.driver = resource_handler.driver


    def wait_until(self, by, value, timeout=5, parent_element=None):
        if parent_element:
            WebDriverWait(parent_element, timeout).until(
                lambda parent_element: self.is_element_present(by, value))
        else:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: self.is_element_present(by, value))

    def is_element_present(self, by, value, parent_element=None):
        self.driver.implicitly_wait(0)
        if parent_element:
            element_or_driver = parent_element
        else:
            element_or_driver = self.driver
        try:
            element_or_driver.find_element(by, value)
            return True
        except:
            NoSuchElementException
            return False
        finally:
            self.driver.implicitly_wait(self.implicit_wait)


class SearchTextElement(BasePageElement):

    locator = 'q'


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
