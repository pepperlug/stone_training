
import random
from model.group import Group

def test_edit_group_by_index(app,db,check_ui):
    # Если групп нет, создаём одну
    if app.group.count_group() == 0:
        app.group.create(Group(name="test"))
    # Получаем список групп из базы до изменения
    old_groups = db.get_group_list()
    # Выбираем случайную группу для редактирования
    group = random.choice(old_groups)
    # Создаём новые данные для группы
    new_data = Group(name="sand", header="sand", footer="sand")
    new_data.id = group.id
    # Редактируем группу
    app.group.edit_group_by_id(group.id, new_data)
    # Получаем список групп из базы после изменения
    new_groups = db.get_group_list()
    # Заменяем старый объект на новый в копии списка
    old_groups[old_groups.index(group)] = new_data
    # Сравниваем списки
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        # Сортируем оба списка по id для корректного сравнения
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
