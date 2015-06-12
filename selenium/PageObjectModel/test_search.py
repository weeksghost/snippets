import os
import unittest
from selenium import webdriver
import page


class GoogleSearch(unittest.TestCase):
    '''Functional test for Google search'''

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://www.google.com')


    def test_search_selenium_from_google(self):
        '''Search selenium from Google.com'''
        self.driver.maximize_window()
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches(), 'Google'
        main_page.search_text_element = 'selenium'
        main_page.click_submit()
        search_results_page = page.SearchResultsPage(self.driver)
        assert search_results_page.is_results_found(), 'No results found.'


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
