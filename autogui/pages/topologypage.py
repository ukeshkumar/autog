import autogui.locators as locators
from autogui.pages.navigationpage import NavigationPage


class TopologyPage (NavigationPage):
    """ Login Page """

    def __init__(self, driver, conf):
        super(TopologyPage, self).__init__(driver, conf)
        self._page_title = "Topology"

    @property
    def reloadBtn(self):
        return self._get_element(*locators.TopologyPage.reloadBtn)
