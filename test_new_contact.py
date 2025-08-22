# -*- coding: utf-8 -*-
from distutils.dep_util import newer_group

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.firefox.options import Options
from features_contact import FeaturesContact
import unittest

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        self.wd = webdriver.Firefox(executable_path=r'C:\Windows\SysWOW64\geckodriver.exe', options=options)
        self.wd.implicitly_wait(30)
    
    def test_new_contact(self):
        wd = self.wd
        self.home_page(wd)
        self.login(wd)
        self.submit_login(wd)
        self.form_new_contact(wd)
        self.add_new_contact(wd,FeaturesContact(firstname="John", middlename="Snow", lastname="Aegon", nickname="Targaryen",title="north", company="night watch", address="black castle",home="111", mobile="222", work="333",fax="dark dozor", email="targaryen@gmail.com", bday="4",bmonth="May",byear="283",new_group = "snow"))
        self.return_to_home(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_home(self, wd):
        wd.find_element_by_link_text("home").click()

    def add_new_contact(self, wd, features_contact):
        #вводим фио и никнейм нового контакта
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(features_contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(features_contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(features_contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(features_contact.nickname)
        # вводим заголовок, компанию, адрес нового контакта
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(features_contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(features_contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(features_contact.address)

        # вводим домашний, рабочий, мобильный телефоны нового контакта
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(features_contact.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(features_contact.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(features_contact.work)
        # вводим доп.способы связи: факс и электронную почту
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(features_contact.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(features_contact.email)
        # Выбираем дату рождения для нового контакта
        Select(wd.find_element_by_name("bday")).select_by_visible_text(features_contact.bday)
        wd.find_element_by_xpath("//option[@value='4']").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(features_contact.bmonth)
        wd.find_element_by_xpath("//option[@value='May']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(features_contact.byear)
        # Выбираем группу для нового контакта
        wd.find_element_by_name("new_group").click()
        Select(wd.find_element_by_name("new_group")).select_by_visible_text(features_contact.new_group)
        wd.find_element_by_xpath("//div[@id='content']/form/select[5]/option[7]").click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()


    def form_new_contact(self, wd):
        wd.find_element_by_link_text("add new").click()

    def submit_login(self, wd):
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def login(self, wd):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")

    def home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
