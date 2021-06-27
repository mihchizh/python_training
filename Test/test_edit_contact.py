from model.Contact import Contact


def test_edit_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.create_new_contact(Contact(firstname="test333"))
    app.contact.edit_first_contact(Contact(firstname="test777"))
