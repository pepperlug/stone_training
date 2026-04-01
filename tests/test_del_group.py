from model.group import Group

def test_del_first_group(app):
    if app.group.count_group() == 0:
        app.group.create(Group(name="test"))
    app.group.del_first_group()
