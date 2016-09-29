from selenium.webdriver.support.ui import WebDriverWait
import selenium.common.exceptions as Exceptions

class BaseObject(object):

    default_timeout = 10

    def __init__(self, driver, conf):
        self.driver = driver
        self.conf = conf

    def _get_element(self, *locator):
        return self.driver.find_element(*locator)

    def _get_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def _fill_field_element(self, data, field_element):
        field_element.clear()
        field_element.send_keys(data)
        return field_element

    def _is_element_visible(self, *locator):
        try:
            return self._get_element(*locator).is_displayed()
        except (Exceptions.NoSuchElementException,
                Exceptions.ElementNotVisibleException):
            return False

    def wait_until(self, locator):
        WebDriverWait(self.driver, self.default_timeout).until(
            lambda driver: driver.find_element(*locator))
