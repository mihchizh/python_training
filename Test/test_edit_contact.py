from model.Contact import Contact


def test_edit_first_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.create_new_contact(Contact(firstname="BSR",lastname="Art"))
    old_contacts = app.contact.get_contact_list()
    contact = (Contact(firstname="ABC", lastname="Baf"))
    app.contact.edit_first_contact(contact)
    assert len(old_contacts) == app.contact.count_contact()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)