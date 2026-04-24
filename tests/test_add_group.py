# -*- coding: utf-8 -*-
from model.group import Group

#теперь здесь параметризованный тест, данные для него получаем из файла data/groups.json
def test_add_group(app,db,json_groups,check_ui):
    group = json_groups
    # Получаем из БД список групп
    old_groups = db.get_group_list()
    #выполняем создание группы
    app.group.create(group)
    #получаем из БД список новых групп
    new_groups = db.get_group_list()
    #добавляем созданную группу в локальный список
    old_groups.append(group)
    #сравниваем группы
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


