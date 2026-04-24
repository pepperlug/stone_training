from pony.orm import *
from datetime import datetime
from model.group import Group
from model.features_contact import FeaturesContact
from pymysql.converters import decoders
class ORMFixture:
    pass
    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str,column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str,column='group_footer')
        contacts = Set(lambda: ORMFixture.ORMContact,table='address_in_groups',column='id',reverse='groups',lazy=True)


    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str,column='firstname')
        middlename = Optional(str,column='middlename')
        lastname = Optional(str, column='lastname')
        nickname = Optional(str, column='nickname')
        fax = Optional(str, column='fax'),
        email = Optional(str, column='email'),
        email2 = Optional(str, column='email2'),
        email3 = Optional(str, column='email3'),
        home = Optional(str, column='home'),
        mobile = Optional(str, column='mobile'),
        work = Optional(str, column='work'),
        title = Optional(str, column='title'),
        company = Optional(str, column='company'),
        address = Optional(str, column='address'),
        bday = Optional(str, column='bday'),
        bmonth = Optional(str, column='bmonth'),
        byear = Optional(str, column='byear')
        groups = Set(lambda:ORMFixture.ORMGroup,table='address_in_groups',column='group_id',reverse='contacts',lazy=True)

    def __init__(self,host,name,user,password,conv=decoders):
        self.db.bind('mysql',host=host,database=name,user=user,password=password)
        self.db.generate_mapping()

    def convert_groups_to_model(self,groups):
        def convert(group):
            return Group(id=str(group.id),name=group.name,header=group.header,footer=group.footer)
        return list(map(convert,groups))

    def convert_contacts_to_model(self,contacts):
        def convert(contact):
            return FeaturesContact(id=str(contact.id),
                                   firstname=contact.firstname,
                                   middlename=contact.middlename,
                                   lastname=contact.lastname,
                                   nickname=contact.nickname,
                                   fax=contact.fax,
                                   email=contact.email,
                                   email2=contact.email2,
                                   email3=contact.email3,
                                   home=contact.home,
                                   mobile=contact.mobile,
                                   work=contact.work,
                                   title=contact.title,
                                   company=contact.company,
                                   address=contact.address,
                                   bday=contact.bday,
                                   bmonth=contact.bmonth,
                                   byear=contact.byear
            )
        return list(map(convert,contacts))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in self.ORMContact))

    @db_session
    def get_contacts_in_group(self,group):
        orm_group = list(select(g for g in self.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(list(orm_group.contacts))

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(
            select(c for c in self.ORMContact if orm_group not in c.groups))

