from model.Contact import Contact


def test_add_contact(app):
    app.session.Login(username="admin", password="secret")
    # create new contact
    app.contact.create_new_contact(
        Contact(firstname="Miha", middlename="testov", lastname="Tetki", nickname="telega", title="ret",
                companyadress="Russia", companyname="auriga", homephone="2222222", mobilephone="3333333",
                workphone="1111111", fax="1234567", email="test@test.ru", email2="test1@test.ru",
                homepage="localrussia.com", bday="2", bmonth="May", byear="1985", group="New group", adress2="Russia 1",
                phone2="Gorky", notes="notes"))
    app.session.Logout()


def test_add_new_contact(app):
    app.session.Login(username="admin", password="secret")
    app.contact.create_new_contact(
        Contact(firstname="Miha1", middlename="testov1", lastname="Tetki1", nickname="telega1", title="ret1",
                companyadress="Russia1", companyname="auriga1", homephone="22222221", mobilephone="33333331",
                workphone="11111111", fax="12345671", email="test1@test.ru", email2="test1@test.ru",
                homepage="localrussia1.com", bday="2", bmonth="May", byear="1985", group="New group",
                adress2="Russia 11", phone2="Gorky1", notes="notes1"))
    app.session.Logout()