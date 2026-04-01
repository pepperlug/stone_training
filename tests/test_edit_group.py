from model.group import Group

def test_edit_group(app):
    if app.group.count_group() == 0:
        app.group.create(Group(name="test"))
    app.group.edit_first_group(Group(name="sand", header="sand", footer="sand"))

def test_edit_first_group_name(app):
    if app.group.count_group() == 0:
        app.group.create(Group(name="test"))
    app.group.edit_first_group(Group(name="octodad"))
