from model.group import Group

def test_edit_group(app):
    app.session.login(user="admin", password="secret")
    app.group.edit_first_group(Group(name="sand", header="sand", footer="sand"))
    app.session.logout()