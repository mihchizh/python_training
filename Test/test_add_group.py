# -*- coding: utf-8 -*-
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.session.Login(username="admin", password="secret")
    app.group.create(Group(name="New group", header="Test header", footer="Test footer"))
    app.session.Logout()

def test_add_empty_group(app):
    app.session.Login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.Logout()

