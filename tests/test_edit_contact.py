import random

from model.features_contact import FeaturesContact

def test_edit_contact_by_index(app,db,check_ui):
    # Если в базе нет контактов, создаем контакт
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

    # Получаем список контактов из БД до редактирования
    old_contacts = db.get_contact_list()

    # Выбираем случайный контакт
    contact = random.choice(old_contacts)

    # Создаем новые данные для редактирования
    new_data = FeaturesContact(
        firstname="Davos",
        middlename="Sivort",
        lastname="Luk",
        nickname="Desni",
        title="dragon stone",
        company="stannys",
        address="black castle",
        home="2234",
        mobile="2224",
        work="3353",
        fax="dark dozor1",
        email="targaryen@gmail.com",
        bday="4",
        bmonth="May",
        byear="283"
    )

    # Сохраняем id редактируемого контакта
    new_data.id = contact.id
    # Редактируем контакт
    app.contact.edit_contact_by_id(new_data, contact.id)
    # Получаем список контактов из БД после редактирования
    new_contacts = db.get_contact_list()
    # Заменяем старый контакт на новый и сравниваем списки
    old_contacts.remove(contact)
    old_contacts.append(new_data)
    assert sorted(old_contacts, key=FeaturesContact.id_or_max) == sorted(new_contacts, key=FeaturesContact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=FeaturesContact.id_or_max) == sorted(app.contact.get_contacts_list(),
                                                                             key=FeaturesContact.id_or_max)
