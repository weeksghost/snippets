from selenium.webdriver.support.ui import WebDriverWait


class BasePageElement(object):

    def __set__(self, obj, value):
        # fetch driver from caller
        driver = obj.driver
        # set element
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_id(self.locator))
        # force focus on element before send_keys
        driver.find_element_by_id(self.locator).click()
        if value.startswith(':no-clear:'):
            value = value.replace(':no-clear:', '')
        else:
            driver.find_element_by_id(self.locator).clear()
        driver.find_element_by_id(self.locator).send_keys(value)

    def __get__(self, obj, owner):
        try:
            driver = obj.driver
        except AttributeError:
            return
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_id(self.locator))
        element = driver.find_element_by_id(self.locator)
        return element.get_attribute("value")