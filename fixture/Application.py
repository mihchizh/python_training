from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.Contact import ContactHelper


class Application:

    def __init__(self, browser, base_url, username, password):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser  %s" % browser)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url
        self.username = username
        self.password = password

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        # open home page
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
