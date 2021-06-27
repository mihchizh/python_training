from model.Contact import Contact


def test_delete_first_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.create_new_contact(Contact(firstname="test333"))
    app.contact.delete_first_contact()

