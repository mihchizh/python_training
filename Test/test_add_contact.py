from model.Contact import Contact


def test_add_contact(app):
    app.contact.create_new_contact(
        Contact(firstname="Miha", middlename="testov", lastname="Tetki", nickname="telega", title="ret",
                company="auriga", address="Russia", home="2222222", mobile="3333333",
                work="1111111", fax="1234567", email="test@test.ru", email2="test1@test.ru",
                homepage="localrussia.com", bday="2", bmonth="May", byear="1985", group="New group", address2="Russia 1",
                phone2="Gorky", notes="notes"))



def test_add_new_contact(app):
    app.contact.create_new_contact(
        Contact(firstname="Miha1", middlename="testov1", lastname="Tetki1", nickname="telega1", title="ret1",
                address="Russia1", company="auriga1", home="22222221", mobile="33333331",
                work="11111111", fax="12345671", email="test1@test.ru", email2="test1@test.ru",
                homepage="localrussia1.com", bday="2", bmonth="May", byear="1985", group="New group",
                address2="Russia 11", phone2="Gorky1", notes="notes1"))
