
def test_del_first_group(app):
    app.session.login(user="admin", password="secret")
    app.group.del_first_group()
    app.session.logout()