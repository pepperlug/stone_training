# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.firefox.options import Options
from attribute_contact import CompanyTitle, Phone, Letters, Fio, DateOfBirth
import unittest

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        self.wd = webdriver.Firefox(executable_path=r'C:\Windows\SysWOW64\geckodriver.exe', options=options)
        self.wd.implicitly_wait(30)
    
    def test_untitled_test_case(self):
        wd = self.wd
        self.home_page(wd)
        self.login(wd)
        self.submit_login(wd)
        self.form_new_contact(wd)
        self.add_fio_and_nickname(wd,Fio(firstname="John", middlename="Snow", lastname="Aegon", nickname="Targaryen"))
        self.add_title_company_address(wd,CompanyTitle(title="north", company="night watch", address="black castle"))
        self.add_phone(wd, Phone(home="111", mobile="222", work="333"))
        self.add_letters(wd, Letters(fax="dark dozor", email="targaryen@gmail.com"))

        self.date_of_birth(wd, DateOfBirth(bday="4",bmonth="May",byear="283"))

        wd.find_element_by_name("new_group").click()
        Select(wd.find_element_by_name("new_group")).select_by_visible_text("snow")
        wd.find_element_by_xpath("//div[@id='content']/form/select[5]/option[7]").click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()

        self.return_to_home(wd)
        self.logout(wd)

    def date_of_birth(self, wd, attribute_contact):
        Select(wd.find_element_by_name("bday")).select_by_visible_text(attribute_contact.bday)
        wd.find_element_by_xpath("//option[@value='4']").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(attribute_contact.bmonth)
        wd.find_element_by_xpath("//option[@value='May']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(attribute_contact.byear)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_home(self, wd):
        wd.find_element_by_link_text("home").click()

    def add_letters(self, wd, letters):
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(letters.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(letters.email)

    def add_phone(self, wd, phone):
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(phone.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(phone.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(phone.work)

    def add_title_company_address(self, wd, company_title):
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(company_title.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(company_title.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(company_title.address)

    def add_fio_and_nickname(self, wd, fio):
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(fio.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(fio.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(fio.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(fio.nickname)

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
