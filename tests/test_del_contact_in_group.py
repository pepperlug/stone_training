import random
from model.features_contact import FeaturesContact
from model.group import Group

def test_delete_contact_from_group(app, orm):
    # создаем группу, если их нет
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test_group"))
    # создаем контакт, если контактов нет
    if len(orm.get_contact_list()) == 0:
        app.contact.create(FeaturesContact(firstname="test_contact"))
    # получаем список всех групп
    groups = orm.get_group_list()
    # ищем группу, в которой уже есть контакты
    group = None
    for g in groups:
        if len(orm.get_contacts_in_group(g)) > 0:
            group = g
            break
    # если подходящей группы нет, берем случайную и добавляем в нее контакт
    if group is None:
        group = random.choice(groups)
        contact = random.choice(orm.get_contact_list())
        app.contact.add_contact_to_group(contact.id, group.name)
    # получаем контакты в выбранной группе
    old_contacts = orm.get_contacts_in_group(group)
    # проверяем, что в группе есть хотя бы один контакт
    assert len(old_contacts) > 0
    # выбираем случайный контакт из группы
    contact = random.choice(old_contacts)
    # удаляем контакт из группы
    app.contact.remove_contact_from_group(contact.id, group.name)
    # проверяем, что контакт действительно удалился
    new_contacts = orm.get_contacts_in_group(group)
    assert len(new_contacts) == len(old_contacts) - 1
    assert contact not in new_contacts