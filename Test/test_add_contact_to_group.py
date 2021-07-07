import random
from model.Contact import  Contact
from model.group import Group


def test_add_contact_to_group(app, orm):
    app.group.create_if_no_groups(orm)
    app.contact.create_if_no_contacts(orm)
    groups = orm.get_group_list()
    group = random.choice(groups)
    contacts = orm.get_contacts_not_in_group(Group(id=group.id))
    if not contacts:
        app.contact.create(Contact(firstname="Name"))
        contacts = orm.get_contacts_not_in_group(Group(id=group.id))
    contact = random.choice(contacts)
    old_contacts_in_group = list(orm.get_contacts_in_group(Group(id=group.id)))
    app.contact.add_to_group_by_id(contact.id, group.name)
    new_contacts_in_group = list(orm.get_contacts_in_group(Group(id=group.id)))
    assert len(old_contacts_in_group) + 1 == len(new_contacts_in_group)