# -*- coding: utf-8 -*-
from Application_new import Application_new
from Contact import Contact
import pytest

@pytest.fixture
def app(request):
    fixture = Application_new()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.Login(username="admin", password="secret" )
    # create new contact
    app.Create_new_contact(Contact(firstname="Miha", middlename="testov", lastname="Tetki", nickname="telega",
        title="ret", companyname="auriga", companyadress="Russia", homephone="2222222", mobilephone="3333333",
        workphone="1111111", fax="1234567", email="test@test.ru", email2="test1@test.ru",
        homepage="localrussia.com", bday="2", bmonth="May", byear="1985", group="New group",
        adress2="Russia 1", phone2="Gorky", notes="notes"))
    app.Logout()

def test_add_new_contact(app):
    app.Login( username="admin", password="secret")
    app.Create_new_contact(Contact(firstname="Miha1", middlename="testov1", lastname="Tetki1", nickname="telega1",
        title="ret1", companyname="auriga1", companyadress="Russia1", homephone="22222221", mobilephone="33333331",   workphone="11111111", fax="12345671", email="test1@test.ru",
        email2="test1@test.ru", homepage="localrussia1.com", bday="2", bmonth="May", byear="1985",group="New group",
        adress2="Russia 11", phone2="Gorky1", notes="notes1"))
    app.Logout()

