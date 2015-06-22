import page
import pytest


class GoogleSearch:


    @pytest.mark.parametrize(('project_name',),
                             [('test1',),])
    def test_search_selenium_from_google(self, resource_hander):
        '''Search selenium from Google.com'''
        main_page = page.MainPage(resource_hander)
        assert main_page.is_title_matches(), 'Google'
        main_page.search_text_element = 'selenium'
        main_page.click_submit()
        search_page_results = page.SearchResultsPage(resource_hander)
        assert search_page_results.is_results_found(), 'No results found.'
