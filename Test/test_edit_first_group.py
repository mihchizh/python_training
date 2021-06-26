from model.group import Group


def test_edit_first_group(app):
    app.session.Login(username="admin", password="secret")
    app.group.edit(Group(name="Edit Group", header="Edit header", footer="Edit footer"))
    app.session.Logout()