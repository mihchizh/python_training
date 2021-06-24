# -*- coding: utf-8 -*-
from model.group import Group
from fixture.Application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.Login(username="admin", password="secret")
    app.create_group1(Group(name="New group", header="Test header", footer="Test footer"))
    app.Logout()

def test_add_empty_group(app):
    app.Login(username="admin", password="secret")
    app.create_group1(Group(name="", header="", footer=""))
    app.Logout()

