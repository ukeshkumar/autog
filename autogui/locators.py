from selenium.webdriver.common.by import By

class LoginPage(object):
    """A class for login page locators"""
    username = (By.XPATH, '//div[1]/input')
    password = (By.XPATH, '//div[2]/input')
    loginBtn = (By.XPATH, '//div[3]/form/fieldset/button')


class TopologyPage(object):
    """ locators for topology page"""
    reloadBtn = (By.XPATH, '//*[@id="pageContent"]/div/div/div/button')


class NodesPage(object):
    """ locators for Nodes page"""
    searchBox = (By.XPATH, '//*[@id="pageContent"]/div/div/input')
    nodesTable = (By.XPATH, '//*[@id="pageContent"]/div/table')


class TopBarRegion(object):
    """ locators for Top Bar"""
    toggle_menu = (By.XPATH, '//*[@id="toggleMenu"]')
    header = (By.CSS_SELECTOR, 'nav.navbar-static-top ng-scope')


class SideBarRegion(object):
    """ locators for Top Bar"""
    side_menu = (By.XPATH, '//*[@id="side-menu"]')
    topology_menuitem = (By.XPATH, '//*[@id="side-menu"]/li[1]')
    nodes_menuitem = (By.XPATH, '//*[@id="side-menu"]/li[2]')
    yang_ui_menuitem = (By.XPATH, '//*[@id="side-menu"]/li[3]')
    yang_visualizer_menuitem = (By.XPATH, '//*[@id="side-menu"]/li[4]')
