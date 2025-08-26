# -*- coding: utf-8 -*-
from fixture.application import Application
from model.group import Group
import pytest

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
    
def test_add_group(app):
    app.session.login(user="admin", password="secret")
    app.group.create(Group(name="stone", header="stone", footer="stone"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(user="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()


