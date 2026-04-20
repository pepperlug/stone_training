# -*- coding: utf-8 -*-
from model.features_contact import FeaturesContact
import random
import pytest
import string

#генератор рандомных строк
def random_string(prefix,maxlen):
    symbols = string.ascii_letters + string.punctuation +string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

#случайные тестовые данные
testdata=[
    FeaturesContact(firstname=firstname,
                    middlename=random_string("lastname",3),
                    lastname=lastname,
                    nickname=random_string("nick",3),
                    title=random_string("title",5),
                    company=random_string("comp",6),
                    address=random_string("addr",8),
                    home=random_string("+7",11),
                    mobile=random_string("+7",11),
                    work=random_string("+7",11),
                    fax=random_string("+7",11),
                    email=random_string("em1",12),
                    email2=random_string("em2",12),
                    email3=random_string("em3",12))

    for firstname in ["",random_string("firstname",10)]
    for lastname in ["",random_string("lastname",7)]
]

@pytest.mark.parametrize("features_contact",testdata,ids=[repr(x) for x in testdata])

def test_new_contact(app,features_contact):
    old_contacts = app.contact.get_contacts_list()
    app.contact.add_new_contact(features_contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(features_contact)
    assert sorted(old_contacts, key=FeaturesContact.id_or_max) == sorted(new_contacts, key=FeaturesContact.id_or_max)

