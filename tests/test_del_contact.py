from model.features_contact import FeaturesContact

def test_del_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.add_new_contact(FeaturesContact(firstname="Jonny", middlename="Snow", lastname="Aegon", nickname="Targaryen", title="north",company="night watch", address="black castle", home="111", mobile="222", work="333",fax="dark dozor", email="targaryen@gmail.com", bday="4", bmonth="May", byear="283"))
    old_contacts = app.contact.get_contacts_list()
    app.contact.del_first_contact()
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) - 1 == len(new_contacts)

