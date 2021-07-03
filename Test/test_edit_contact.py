from model.Contact import Contact
from random import randrange

def test_edit_contact_by_index(app):
    if app.contact.count_contact() == 0:
        app.contact.create_new_contact(Contact(firstname="BSR",lastname="Art"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = (Contact(firstname="ABC", lastname="Baf"))
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count_contact()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)