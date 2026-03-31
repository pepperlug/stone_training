from model.group import Group

def test_edit_group(app):
    app.group.edit_first_group(Group(name="sand", header="sand", footer="sand"))

def test_edit_first_group_name(app):
    app.group.edit_first_group(Group(name="sand"))
