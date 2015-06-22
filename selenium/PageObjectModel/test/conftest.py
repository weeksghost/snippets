import pytest

from selenium import webdriver


class ResourceHandler(object):

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('http://google.com')


    def release(self):
        self.driver.close()
        self.driver.quit()


def _release_resource_handler(handler):
    """Teardown method"""
    handler.release()


def _get_resource_handler():
    """ResourceHandler instance"""
    resource_handler = ResourceHandler()
    return resource_handler


@pytest.fixture
def resource_handler(request):
    """ResourceHandler function"""
    return request.cached_setup(
        setup=_get_resource_handler,
        teardown=_release_resource_handler,
        scope='function')
