from model.Contact import Contact
import string
import random
import pytest

def random_string(prefix, maxlen):
    simbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(simbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", lastname="")] + [Contact(firstname=random_string("firstname", 10),
                                                            lastname=random_string("lastname", 10)) for i in range(5)]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_new_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count_contact()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



#def test_add_new_contact(app):
   # app.contact.create_new_contact(
       # Contact(firstname="Miha1", middlename="testov1", lastname="Tetki1", nickname="telega1", title="ret1",
                #address="Russia1", company="auriga1", home="22222221", mobile="33333331",
                #work="11111111", fax="12345671", email="test1@test.ru", email2="test1@test.ru",
                #homepage="localrussia1.com", bday="2", bmonth="May", byear="1985", group="New group",
                #address2="Russia 11", phone2="Gorky1", notes="notes1"))
