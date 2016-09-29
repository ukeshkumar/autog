import autogui.locators as locators
from autogui.pages.navigationpage import NavigationPage


class NodesPage (NavigationPage):
    """ Login Page """

    def __init__(self, driver, conf):
        super(NodesPage, self).__init__(driver, conf)
        self._page_title = "Nodes"

    @property
    def searchNodes(self):
        return self._get_element(*locators.NodesPage.searchBox)

    @property
    def nodesTable(self):
        return self._get_element(*locators.NodesPage.nodesTable)

