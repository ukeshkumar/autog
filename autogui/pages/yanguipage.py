import autogui.locators as locators
from autogui.pages.navigationpage import NavigationPage


class YangUIPage (NavigationPage):
    """ Login Page """

    def __init__(self, driver, conf):
        super(YangUIPage, self).__init__(driver, conf)
        self._page_title = "Yang UI"

