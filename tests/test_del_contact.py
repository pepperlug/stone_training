from model.features_contact import FeaturesContact

def test_del_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.add_new_contact(FeaturesContact(firstname="Jonny", middlename="Snow", lastname="Aegon", nickname="Targaryen", title="north",company="night watch", address="black castle", home="111", mobile="222", work="333",fax="dark dozor", email="targaryen@gmail.com", bday="4", bmonth="May", byear="283"))
    app.contact.del_first_contact()
    app.session.open_home_page()
