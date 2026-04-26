from model.features_contact import FeaturesContact
from model.group import Group

def test_add_contact_to_group(app, db,orm):
    # Получаем все контакты
    contacts = db.get_contact_list()
    # Получаем все группы
    groups = db.get_group_list()
    # Если в базе нет ни одного контакта, создаём тестовый контакт
    if len(contacts) == 0:
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

        # После создания заново получаем список контактов из базы
        contacts = db.get_contact_list()

    # Если в базе нет ни одной группы, создаём тестовую группу
    if len(groups) == 0:
        app.group.create(Group(name="test_group"))
        # После создания заново получаем список групп из базы
        groups = db.get_group_list()
    # Здесь храним контакт, которого ещё нет в выбранной группе
    contact = None
    # Здесь храним группу, в которую будем добавлять контакт
    group = None
    # Перебираем все группы и ищем такую, в которой есть хотя бы один контакт, не состоящий в этой группе
    for current_group in groups:
        # Получаем список контактов, которые НЕ входят в текущую группу
        contacts_not_in_group = orm.get_contacts_not_in_group(current_group)
        # Если такие контакты есть, выбираем первый из них
        if len(contacts_not_in_group) > 0:
            contact = contacts_not_in_group[0]
            # Запоминаем группу, в которой этот контакт пока ещё не состоит
            group = current_group
            # Как только нашли подходящую пару, выходим
            break

    # Если подходящую пару не удалось найти, создаём новый контакт, который не состоит ни в одной группе
    if contact is None:
        app.contact.add_new_contact(FeaturesContact(
            firstname="New",
            lastname="User"
        ))
        # Снова получаем список контактов
        contacts = db.get_contact_list()
        # Берём последнего созданного контакта из списка
        contact = contacts[-1]
        # Для нового контакта выбираем первую доступную группу
        group = groups[0]
    # Добавляем выбранный контакт в выбранную группу
    app.contact.add_contact_to_group(contact.id, group.name)
    # Проверяем, что контакт появился в списке контактов группы
    assert contact in orm.get_contacts_in_group(group)