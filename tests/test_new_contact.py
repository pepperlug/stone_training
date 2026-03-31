# -*- coding: utf-8 -*-
from model.features_contact import FeaturesContact

def test_new_contact(app):
    app.contact.add_new_contact(FeaturesContact(firstname="Jonny", middlename="Snow", lastname="Aegon", nickname="Targaryen",title="north", company="night watch", address="black castle",home="111", mobile="222", work="333",fax="dark dozor", email="targaryen@gmail.com", bday="4",bmonth="May",byear="283",new_group = "stone"))

def test_new_contact_nophone(app):
    app.contact.add_new_contact(FeaturesContact(firstname="Jonny", middlename="Snow", lastname="Aegon", nickname="Targaryen",title="north", company="night watch", address="black castle",home="111", mobile="222", work="333",fax="dark dozor"))
