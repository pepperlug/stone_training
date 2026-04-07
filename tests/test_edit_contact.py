from random import randrange

from model.features_contact import FeaturesContact

def test_edit_contact_by_index(app):
    if app.contact.count_contact() == 0:
        app.contact.add_new_contact(FeaturesContact(firstname="Sansa", middlename="Snow", lastname="Aegon", nickname="Targaryen", title="north",company="night watch", address="black castle", home="111", mobile="222", work="333",fax="dark dozor", email="targaryen@gmail.com", bday="4", bmonth="May", byear="283"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    contact = FeaturesContact(firstname="Davos", middlename="Sivort", lastname="Luk", nickname="Desni", title="dragon stone",company="stannys", address="black castle", home="2234", mobile="2224", work="3353",fax="dark dozor1", email="targaryen@gmail.com", bday="4", bmonth="May", byear="283")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(contact,index)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=FeaturesContact.id_or_max) == sorted(new_contacts, key=FeaturesContact.id_or_max)
