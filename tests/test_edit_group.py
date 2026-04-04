from model.group import Group

def test_edit_group(app):
    if app.group.count_group() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    group = Group(name="sand", header="sand", footer="sand")
    group.id = old_groups[0].id
    app.group.edit_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_edit_first_group_name(app):
    if app.group.count_group() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name="octodad"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
