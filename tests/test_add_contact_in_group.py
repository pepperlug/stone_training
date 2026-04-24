from model.features_contact import FeaturesContact
from model.group import Group

def test_add_contact_to_group(app, db,orm):
    # получаем список контактов и групп из БД
    contact_list = db.get_contact_list()
    group_list = db.get_group_list()
    # если контактов нет — создаем
    if len(contact_list) == 0:
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
        contact_list = db.get_contact_list()
    # если групп нет — создаем
    if len(group_list) == 0:
        app.group.create(Group(name="test_group"))
        group_list = db.get_group_list()
    # берем первый контакт и первую группу
    contact = contact_list[0]
    group = group_list[0]
    # добавляем контакт в группу по названию группы
    app.contact.add_contact_to_group(contact.id, group.name)
    # проверяем, что контакт действительно добавился в группу в БД
    new_contact_list = orm.get_contacts_in_group(group)
    assert contact in new_contact_list