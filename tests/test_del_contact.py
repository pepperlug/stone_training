import random

from model.features_contact import FeaturesContact

def test_del_contact_by_index(app,db,check_ui):
    # Если в базе нет контактов, создаем тестовый контакт
    if len(db.get_contact_list()) == 0:
        app.contact.add_new_contact(FeaturesContact(
            firstname="Jonny",
            middlename="Snow",
            lastname="Aegon",
            nickname="Targaryen",
            title="north",
            company="night watch",
            address="black castle",
            home="111",
            mobile="222",
            work="333",
            fax="dark dozor",
            email="targaryen@gmail.com",
            bday="4",
            bmonth="May",
            byear="283"
        ))
    # Получаем список контактов из базы до удаления
    old_contacts = db.get_contact_list()
    # Выбираем случайный контакт
    contact = random.choice(old_contacts)
    # Удаляем контакт по id
    app.contact.del_contact_by_id(contact.id)
    # Получаем список контактов из базы после удаления
    new_contacts = db.get_contact_list()
    # Удаляем контакт из старого списка и сравниваем списки
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=FeaturesContact.id_or_max) == sorted(app.contact.get_contacts_list(),
                                                                             key=FeaturesContact.id_or_max)

