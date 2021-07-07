from model.Contact import Contact
import random

def test_edit_contact_by_index(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_new_contact(Contact(firstname="BSR",lastname="Art"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    index = old_contacts.index(contact)
    new_contact = (Contact(firstname="ABC", lastname="Baf"))
    app.contact.edit_contact_by_id(contact.id, new_contact)
    assert len(old_contacts) == app.contact.count_contact()
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)