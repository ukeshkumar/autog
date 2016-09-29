import autogui.locators as locators
from autogui.pages.basepage import BasePage
from autogui.pages.topologypage import TopologyPage

class LoginPage (BasePage):
    """ Login Page """

    def __init__(self, driver, conf):
        super(LoginPage, self).__init__(driver, conf)
        self._page_title = "Login"

    @property
    def username(self):
        return self._get_element(*locators.LoginPage.username)

    @property
    def password(self):
        return self._get_element(*locators.LoginPage.password)

    @property
    def loginBtn(self):
        return self._get_element(*locators.LoginPage.loginBtn)

    def login(self, user=None, password=None):
        return self._do_login(user, password)

    def _do_login(self, username, password):
        if username is None:
            username = self.conf["credential"]["username"]
        if password is None:
            password = self.conf["credential"]["password"]
        self.username.send_keys(username)
        self.password.send_keys(password)
        self.loginBtn.click()
#        self.password.send_keys(Keys.RETURN)
        return TopologyPage(self.driver, self.conf)
