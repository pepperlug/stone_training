def test_del_contact(app):
    app.contact.del_first_contact()
    app.session.open_home_page()
