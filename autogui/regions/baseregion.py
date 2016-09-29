from selenium.webdriver.support.ui import WebDriverWait

from autogui.baseobject import BaseObject

class BaseRegion(BaseObject):
    def __init__(self, driver, conf):
        super(BaseRegion, self).__init__(driver, conf)
