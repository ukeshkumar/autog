import time

from autogui.baseobject import BaseObject


class BasePage(BaseObject):

    def __init__(self, driver, conf, baseUrl = ""):
        super(BasePage, self).__init__(driver, conf)
        self._page_title = None
        self.baseUrl = baseUrl

    def open(self, url = "", timeout = None, waitLocator = None):
        self.driver.get(self.baseUrl + url)
        if timeout:
            time.sleep(timeout)
        if waitLocator:
            self.wait_until(waitLocator)

    @property
    def page_title(self):
        return self.driver.title

    def close_window(self):
        return self.driver.close()

    def get_url_current_page(self):
        return self.driver.current_url

    def go_to_previous_page(self):
        self.driver.back()

    def go_to_next_page(self):
        self.driver.forward()

    def refresh_page(self):
        self.driver.refresh()
