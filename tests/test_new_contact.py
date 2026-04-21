# -*- coding: utf-8 -*-
from model.features_contact import FeaturesContact

#теперь здесь параметризованный тест, данные для него получаем из файла data/features_contact.json
def test_new_contact(app,json_features_contact):
    features_contact = json_features_contact
    old_contacts = app.contact.get_contacts_list()
    app.contact.add_new_contact(features_contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(features_contact)
    assert sorted(old_contacts, key=FeaturesContact.id_or_max) == sorted(new_contacts, key=FeaturesContact.id_or_max)

