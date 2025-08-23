# -*- coding: utf-8 -*-

from application import Application
from features_contact import FeaturesContact
import pytest


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
    
def test_new_contact(app):
    app.login(user="admin", password="secret")
    app.form_new_contact()
    app.add_new_contact(FeaturesContact(firstname="John", middlename="Snow", lastname="Aegon", nickname="Targaryen",title="north", company="night watch", address="black castle",home="111", mobile="222", work="333",fax="dark dozor", email="targaryen@gmail.com", bday="4",bmonth="May",byear="283",new_group = "jojo"))
    app.logout()

