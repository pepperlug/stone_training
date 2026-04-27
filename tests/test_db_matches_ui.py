from model.group import Group
from model.features_contact import FeaturesContact
import re


def clear(s):
    return re.sub("[() \-\.]", "", s)


def merge_phones_like_on_home_page(features_contact):
    # Склеиваем все телефоны в строку, как они отображаются на главной странице
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [features_contact.home,
                                        features_contact.mobile,
                                        features_contact.work]))))


def merge_email_like_on_home_page(features_contact):
    # Склеиваем все е-мейлы в строку, как они отображаются на главной странице
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [features_contact.email,
                                    features_contact.email2,
                                    features_contact.email3])))

#тест для сравнения групп из UI и групп из БД
def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)

#тест для сравнения контактов с главной страницы, из UI, и контактов из БД
def test_contact_list(app, db):
    # Если в базе нет ни одного контакта, создаем тестовый контакт
    if len(db.get_contact_list()) == 0:
        app.contact.add_new_contact(FeaturesContact(firstname="Jonny",
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
    # Получаем список контактов из интерфейса
    ui_list = sorted(app.contact.get_contacts_list(), key=FeaturesContact.id_or_max)
    # Приводим контакты из БД к формату, как они отображаются на главной странице
    def clean(contact):
        return FeaturesContact(
            id=contact.id,
            firstname=contact.firstname.strip() if contact.firstname else "",
            lastname=contact.lastname.strip() if contact.lastname else "",
            address=contact.address.strip() if contact.address else "",
            all_phones_from_page=merge_phones_like_on_home_page(contact),
            all_email_from_page=merge_email_like_on_home_page(contact)
        )
    # Получаем список контактов из БД и приводим к списку
    db_list = sorted(map(clean, db.get_contact_list()), key=FeaturesContact.id_or_max)
    # Попарно сравниваем каждый контакт (включая телефоны и email)
    for ui_contact, db_contact in zip(ui_list, db_list):
        assert ui_contact.firstname == db_contact.firstname
        assert ui_contact.lastname == db_contact.lastname
        assert ui_contact.address == db_contact.address
        assert ui_contact.all_phones_from_page == db_contact.all_phones_from_page
        assert ui_contact.all_email_from_page == db_contact.all_email_from_page


