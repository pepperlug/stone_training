def test_del_contact(app):
    app.session.login(user="admin", password="secret")
    app.contact.del_first_contact()
    app.session.open_home_page()
    app.session.logout()