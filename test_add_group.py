# -*- coding: utf-8 -*-
from application import Application
from group import Group
import pytest

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
    
def test_add_group(app):
    app.login(user="admin", password="secret")
    app.add_new_group(Group(name="stone", header="stone", footer="stone"))
    app.logout()

def test_add_empty_group(app):
    app.login(user="admin", password="secret")
    app.add_new_group(Group(name="", header="", footer=""))
    app.logout()


