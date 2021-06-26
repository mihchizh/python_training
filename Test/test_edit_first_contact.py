from model.Contact import Contact


def test_edit_first_contact(app):
    app.session.Login(username="admin", password="secret")
    # create new contact
    app.contact.edit_first_contact(
        Contact(firstname="Miha2", middlename="testov2", lastname="Tetki2", nickname="telega2", title="ret2",
                companyadress="Russia2", companyname="auriga2", homephone="22222222", mobilephone="33333332",
                workphone="11111112", fax="12345672", email="test@test.ru2", email2="test12@test.ru",
                homepage="localrussia.com", bday="2", bmonth="May", byear="1985", group="New group", adress2="Russia 12",
                phone2="Gorky2", notes="notes2"))
    app.session.Logout()


