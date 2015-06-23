import page
import pytest
from unittestzero import Assert

from page.home import HomePage
from page.home import SearchResultsPage
from base_test import BaseTest


class TestGoogleSearch(BaseTest):

    @pytest.mark.nondestructive
    def test_search_selenium_from_google(self, mozwebqa):
        '''Search selenium from Google.com'''
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()




        #main_page = page.MainPage()
        #main_page.driver.get('http://google.com')
        #assert main_page.is_title_matches(), 'Google'
        #main_page.search_text_element = 'selenium'
        #main_page.click_submit()
        #search_page_results = page.SearchResultsPage()
        #assert search_page_results.is_results_found(), 'No results found.'
