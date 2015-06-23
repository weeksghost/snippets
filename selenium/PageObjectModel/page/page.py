from element import BasePageElement
from locators import MainPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from unittestzero import Assert


class Page(object):
    '''Base page object'''

    implicit_wait = 10

    def __init__(self, testsetup):
        self.testsetup = testsetup
        self.base_url = testsetup.base_url
        self.selenium = testsetup.selenium
        self.timeout = testsetup.timeout

    def open(self):
        self.selenium.get(self.base_url)

    @property
    def page_title(self):
        WebDriverWait(self.selenium, self.timeout).until(lambda s: self.selenium.title)
        return self.selenium.title

    @property
    def is_the_current_page(self):
        if self._page_title:
            Assert.equal(self.page_title, self._page_title,
                         "Expected page title: %s. Actual page title: %s" % (self._page_title, self.page_title))
        return True

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

    def get_url_current_page(self):
        return(self.selenium.current_url)


class PageRegion(Page):
    """Base class for a page region (generally an element in a list of elements)."""

    def __init__(self, testsetup, element):
        self._root_element = element
        Page.__init__(self, testsetup)
