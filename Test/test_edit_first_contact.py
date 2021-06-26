from model.Contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name = "test"))
    app.contact.edit_first_contact(Contact(middlename="testov2"))
