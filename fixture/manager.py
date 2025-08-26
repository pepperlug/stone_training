from fixture.contact import ContactHelper
from fixture.session import SessionHelper
from fixture.groups import GroupHelper

class Manager:
    def __init__(self):
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)