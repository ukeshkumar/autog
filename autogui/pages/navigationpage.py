from autogui.pages.basepage import BasePage
from autogui.regions import bars


class NavigationPage(BasePage):

    @property
    def header(self):
        return bars.TopBarRegion(self.driver, self.conf)

    @property
    def side_menu(self):
        return bars.SideBarRegion(self.driver, self.conf)
