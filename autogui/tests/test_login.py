import json
import unittest
import time

import selenium.common.exceptions as Exceptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


from autogui.pages.loginpage import LoginPage
import autogui.locators as locators


class test_loginpage(unittest.TestCase):
    """ to test login page"""

    def setUp(self):
        self.driver = webdriver.Firefox()
#        self.driver.implicitly_wait = 1

#    def tearDown(self):
#        self.driver.close()

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)

        json_data = open("autogui/config.json").read()  # 'opening new configuration file and reading it'
        self.data = json.loads(json_data)

    def test_login(self):
        login_pg = LoginPage(self.driver, self.data)
        login_pg.open(self.data["controller"]["url"], waitLocator=locators.LoginPage.loginBtn)

        self.topology_pg = login_pg.login("admin", "root123")


#    def test_topology(self):
#        if self.topology_pg:
#            self.topology_pg.side_menu.nodes_menuitem.click()


if __name__ == "__main__":
    unittest.main()

