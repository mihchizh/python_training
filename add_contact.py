# -*- coding: utf-8 -*-
from selenium import webdriver

from selenium.webdriver.support.ui import Select
from Contact import Contact
import unittest

class AddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        self.Login(wd, username="admin", password="secret" )
        # create new cotact
        self.Create_new_contact(wd, Contact(firstname="Miha", middlename="testov", lastname="Tetki", nickname="telega",
                           title="ret", companyname="auriga", companyadress="Russia", homephone="2222222", mobilephone="3333333",
                           workphone="1111111", fax="1234567", email="test@test.ru", email2="test1@test.ru",
                           homepage="localrussia.com", bday="2", bmonth="May", byear="1985", group="New group",
                           adress2="Russia 1", phone2="Gorky", notes="notes"))


        # home page
        self.home_page(wd)
        self.Logout(wd)

    def test_add_new_contact(self):
        wd = self.wd
        self.Login(wd, username="admin", password="secret")
        # create new cotact
        self.Create_new_contact(wd, Contact(firstname="Miha1", middlename="testov1", lastname="Tetki1", nickname="telega1",
                                            title="ret1", companyname="auriga1", companyadress="Russia1",
                                            homephone="22222221", mobilephone="33333331",
                                            workphone="11111111", fax="12345671", email="test1@test.ru",
                                            email2="test1@test.ru",
                                            homepage="localrussia1.com", bday="2", bmonth="May", byear="1985",
                                            group="New group",
                                            adress2="Russia 11", phone2="Gorky1", notes="notes1"))

        # home page
        self.home_page(wd)
        self.Logout(wd)


    def Logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def Create_new_contact(self, wd, Contact):
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(Contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(Contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(Contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(Contact.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(Contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(Contact.companyname)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(Contact.companyadress)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(Contact.homephone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(Contact.mobilephone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(Contact.workphone)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(Contact.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(Contact.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(Contact.email2)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(Contact.homepage)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(Contact.bday)
        wd.find_element_by_xpath("//option[@value='2']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(Contact.bmonth)
        wd.find_element_by_xpath("//option[@value='May']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(Contact.byear)
        wd.find_element_by_name("new_group").click()
        Select(wd.find_element_by_name("new_group")).select_by_visible_text(Contact.group)
        wd.find_element_by_xpath("//div[@id='content']/form/select[5]/option[4]").click()
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(Contact.adress2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(Contact.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(Contact.notes)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def Login(self, wd, username, password):
        wd.get("http://localhost/addressbook/group.php")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
