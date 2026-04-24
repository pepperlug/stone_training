import random
from model.group import Group

def test_del_some_group(app,db,check_ui):
    # Если в базе данных нет групп, создаем одну
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    # Получаем список групп из БД перед удалением
    old_groups = db.get_group_list()
    # Выбираем случайную группу из списка для удаления
    group = random.choice(old_groups)
    #Удаляем выбранную группу через пользовательский интерфейс
    app.group.del_group_by_id(group.id)
    # Получаем новый список групп из БД после удаления
    new_groups = db.get_group_list()
    # Удаляем выбранную группу из нашего локального "старого" списка
    old_groups.remove(group)
    #Сравниваем списки из БД
    assert old_groups == new_groups
    if check_ui:
        # Сортируем оба списка по id для корректного сравнения
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)