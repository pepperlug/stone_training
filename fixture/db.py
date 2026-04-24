import pymysql

from model.features_contact import FeaturesContact
from model.group import Group

class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection =  pymysql.connect(host=host,database=name,user=user,password=password,autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id,name,header,footer) = row
                list.append(Group(id=str(id),name=name,header=header,footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, middlename, lastname, nickname, fax, email, email2, email3, home, mobile, work, title, company, address, bday, bmonth, byear from addressbook")
            for row in cursor:
                (id,firstname,middlename,lastname,nickname,fax,email,email2,email3,home,mobile,work,title,company,address,bday,bmonth,byear) = row
                list.append(FeaturesContact(id=str(id),
                                            firstname=firstname,
                                            lastname=lastname,
                                            middlename=middlename,
                                            nickname=nickname,
                                            fax=fax,
                                            email=email,
                                            email2=email2,
                                            email3=email3,
                                            home=home,
                                            mobile=mobile,
                                            work=work,
                                            title=title,
                                            company=company,
                                            address=address,
                                            bday=bday,
                                            bmonth=bmonth,
                                            byear=byear))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()