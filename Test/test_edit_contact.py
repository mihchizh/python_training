from model.Contact import Contact


def test_edit_first_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.create_new_contact(Contact(firstname="test333"))
    old_contacts = app.contact.get_contact_list()
    contact = (Contact(firstname="Test777"))
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)