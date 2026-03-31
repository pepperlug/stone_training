from model.features_contact import FeaturesContact

def test_edit_first_contact(app):
    app.contact.edit_first_contact(FeaturesContact(firstname="Davos", middlename="Sivort", lastname="Luk", nickname="Desni", title="dragon stone",company="stannys", address="black castle", home="2234", mobile="2224", work="3353",fax="dark dozor1", email="targaryen@gmail.com", bday="4", bmonth="May", byear="283",new_group="sand"))
