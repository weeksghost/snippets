import os
import unittest
import requests
from selenium import webdriver
import selenium.webdriver.support.ui as ui


class SearchTests(unittest.TestCase):

    domain = domain

    def setUp(self):
        self.driver = webdriver.PhantomJS('phantomjs',
                      service_log_path=os.path.devnull)
        self.driver.implicitly_wait(30)


    def tearDown(self):
        self.driver.quit()


    def test_search_1200(self):
        """
        @1200 search from homepage and verify result
        """
        self.driver.get(self.domain)
        self.driver.maximize_window()
        self.assertTrue(u'TITLE' in
        self.driver.page_source, 'Title text not found')
        search = self.driver.find_element_by_css_selector("#XXXX")
        wait = ui.WebDriverWait(self.driver, 5)
        search.clear()
        search.send_keys("XXXX")
        search.submit()
        try:
          wait.until(lambda driver: u"XXXX" in
          self.driver.find_element_by_css_selector("xxxx > a").text,
                                                    'Not found!')
        except:
          current_url = self.driver.current_url
          resp = requests.get(current_url)
          if resp.status_code != 200:
            raise Exception("Search failed! => [%s] %s" % (resp.status_code,
                                                            current_url))


    def test_search_720(self):
        """
        @720 search from homepage and verify result
        """
        self.driver.get(self.domain)
        self.assertTrue(u'XXXX' in
        self.driver.page_source, 'Title text not found')
        search = self.driver.find_element_by_css_selector("#XXXX")
        wait = ui.WebDriverWait(self.driver, 5)
        search = self.driver.find_element_by_css_selector("#XXXX")
        search.click()
        search_field = self.driver.find_element_by_css_selector("#XXXX")
        search_field.send_keys("XXXX")
        search_field.submit()
        try:
          wait.until(lambda driver: u"XXXX" in
          self.driver.find_element_by_css_selector("xxxx > a").text,
                                                    'Not found!')
        except:
          current_url = self.driver.current_url
          resp = requests.get(current_url)
          if resp.status_code != 200:
            raise Exception("Search failed! => [%s] %s" % (resp.status_code,
                                                            current_url))


if __name__ == '__main__':
    unittest.main()
