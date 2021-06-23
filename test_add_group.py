# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from group import Group
import unittest

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    
    def test_add_group(self):
        wd = self.wd
        self.Login(wd, username="admin", password="secret")
        self.create_group1(wd, Group(name="New group", header="Test header", footer="Test footer"))
        self.return_to_group_page(wd)
        self.Logout(wd)
    def test_add_empty_group(self):
        wd = self.wd
        self.Login(wd, username="admin", password="secret")
        self.create_group1(wd, Group(name="", header="", footer=""))
        self.return_to_group_page(wd)
        self.Logout(wd)
    def Logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()

    def create_group1(self, wd, group):
        # init group creation
        self.open_groups_page(wd)
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        self.create_group(wd)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()

    def return_to_group_page(self, wd):
        # return to group page
        wd.find_element_by_link_text("group page").click()

    def create_group(self, wd):
        wd.find_element_by_name("group_footer").click()

    def open_groups_page(self, wd):
        # open groups page
        wd.find_element_by_link_text("groups").click()

    def Login(self, wd, username, password):
        self.open_home_page(wd)
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        # open home page
        wd.get("http://localhost/addressbook/group.php?selected%5B%5D=1&delete=Delete+group%28s%29")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    

    
    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
