# -*- coding: utf-8 -*-
from model.features_contact import FeaturesContact

#теперь здесь параметризованный тест, данные для него получаем из файла data/features_contact.json
def test_new_contact(app,json_features_contact,db,check_ui):
    features_contact = json_features_contact
    # Получаем список контактов из базы до добавления
    old_contacts = db.get_contact_list()
    # Добавляем новый контакт через интерфейс
    app.contact.add_new_contact(features_contact)
    # снова запрашиваем контакты из БД
    new_contacts = db.get_contact_list()
    # Добавляем новый контакт в локальный список для сравнения
    old_contacts.append(features_contact)
    # Сравниваем списки из базы
    assert sorted(old_contacts, key=FeaturesContact.id_or_max) == sorted(new_contacts, key=FeaturesContact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=FeaturesContact.id_or_max) == sorted(app.contact.get_contacts_list(),
                                                                             key=FeaturesContact.id_or_max)

