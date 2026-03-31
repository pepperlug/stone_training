#здесь вспомогательные классы для атрибутов нового контакта
class FeaturesContact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, fax=None, email=None,home=None,mobile=None,work=None,title=None, company=None, address=None,bday=None, bmonth=None, byear=None,new_group=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.fax = fax
        self.email = email
        self.home = home
        self.mobile = mobile
        self.work = work
        self.title = title
        self.company = company
        self.address = address
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.new_group = new_group
