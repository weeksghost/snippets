import page
import pytest
import unittest
from conftest import resource_handler


class GoogleSearch(unittest.TestCase):

    @pytest.mark.usefixtures('resource_handler')
    def test_search_selenium_from_google(self, resource_handler=resource_handler):
        '''Search selenium from Google.com'''
        main_page = page.MainPage(resource_handler)
        assert main_page.is_title_matches(), 'Google'
        main_page.search_text_element = 'selenium'
        main_page.click_submit()
        search_page_results = page.SearchResultsPage(resource_handler)
        assert search_page_results.is_results_found(), 'No results found.'


if __name__ == '__main__':
    unittest.main()
