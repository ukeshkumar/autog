from autogui.regions.baseregion import BaseRegion
from autogui import locators


class TopBarRegion(BaseRegion):

    @property
    def header(self):
        return self._get_element(*locators.TopBarRegion.header)

    @property
    def toggle_menu(self):
        return self._get_element(*locators.TopBarRegion.toggle_menu)


class SideBarRegion(BaseRegion):

    @property
    def side_menu(self):
        return self._get_element(*locators.SideBarRegion.side_menu)

    @property
    def topology_menuitem(self):
        return self._get_element(*locators.SideBarRegion.topology_menuitem)

    @property
    def nodes_menuitem(self):
        return self._get_element(*locators.SideBarRegion.nodes_menuitem)

    @property
    def yang_ui_menuitem(self):
        return self._get_element(*locators.SideBarRegion.yang_ui_menuitem)

    @property
    def yang_visualizer_menuitem(self):
        return self._get_element(*locators.SideBarRegion.yang_visualizer_menuitem)

    def is_menu_displayed(self):
        return self._is_element_visible(*locators.SideBarRegion.side_menu)
