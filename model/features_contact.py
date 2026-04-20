#здесь вспомогательные классы для атрибутов нового контакта
from sys import maxsize

class FeaturesContact:
    def __init__(self, firstname=None,
                 middlename=None,
                 lastname=None,
                 nickname=None,
                 fax=None,
                 email=None,
                 email2=None,
                 email3=None,
                 home=None,
                 mobile=None,
                 work=None,
                 title=None,
                 company=None,
                 address=None,
                 bday=None,
                 bmonth=None,
                 byear=None,
                 new_group=None,
                 id=None,
                 all_phones_from_page=None,
                 all_email_from_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.fax = fax
        self.email = email
        self.email2=email2
        self.email3=email3
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
        self.id = id
        self.all_phones_from_page=all_phones_from_page
        self.all_email_from_page = all_email_from_page

    def __repr__(self):
        parts = [str(self.id)]

        for value in [
            self.firstname,
            self.lastname,
            self.middlename,
            self.nickname,
            self.title,
            self.company,
            self.address,
            self.home,
            self.mobile,
            self.work,
            self.fax,
            self.email,
            self.email2,
            self.email3
        ]:
            if value is not None and value != "":
                parts.append(value)

        return ":".join(parts)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize