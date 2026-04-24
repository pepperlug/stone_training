from model.group import Group
from model.features_contact import FeaturesContact

#тест для сравнения групп из UI и групп из БД
def test_group_list(app,db):
    ui_list = app.group.get_group_list()
    def clean(group):
        return Group(id=group.id,name=group.name.strip())
    db_list = map(clean,db.get_group_list())
    assert sorted(ui_list,key=Group.id_or_max) == sorted(db_list,key=Group.id_or_max)

#тест для сравнения контактов с главной страницы, из UI, и контактов из БД
def test_contact_list(app,db):
    #Если в базе нет контактов, создаем тестовый контакт
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
    # Получаем список контактов из UI
    ui_list = app.contact.get_contacts_list()

    # Функция для очистки данных из БД перед сравнением
    def clean(contact):
        return FeaturesContact(
            id=contact.id,
            firstname=contact.firstname.strip(),
            lastname=contact.lastname.strip(),
            address=contact.address.strip(),
            all_phones_from_page=contact.all_phones_from_page,
            all_email_from_page=contact.all_email_from_page
        )
    #Получаем список контактов из БД
    db_list = map(clean, db.get_contact_list())
    # Сравниваем списки контактов из UI и БД
    assert sorted(ui_list, key=FeaturesContact.id_or_max) == sorted(db_list, key=FeaturesContact.id_or_max)


