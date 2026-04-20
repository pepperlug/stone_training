from selenium.webdriver.support.ui import Select
from model.features_contact import FeaturesContact
import re
class ContactHelper:
    def __init__(self,app):
        self.app = app

    #переход на форму создания нового контакта
    def form_contact(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("photo")) > 0):
            wd.find_element_by_link_text("add new").click()

    # создание нового контакта
    def add_new_contact(self,features_contact):
        wd = self.app.wd
        self.form_contact()
        self.input_features_contact(features_contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
        self.contacts_cache = None

    #обновление данных контакта
    def update_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    #удаление первого контакта в списке
    def del_first_contact(self):
        self.del_contact_by_index(0)

    #удаление случайного контакта в списке
    def del_contact_by_index(self,index):
        wd = self.app.wd
        #переход на форму существующих контактов
        self.home_page(wd)
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.contacts_cache = None

    def edit_first_contact(self, features_contact,index):
        self.edit_contact_by_index(0,features_contact)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.home_page(wd)
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    #редактирование первого контакта в списке
    def edit_contact_by_index(self,index,features_contact):
        self.open_contact_to_edit_by_index(index)
        self.input_features_contact(features_contact)
        self.update_contact()
        self.contacts_cache = None

    def home_page(self, wd):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home").click()

    #работа с атрибутами контакта
    def input_features_contact(self, features_contact):
        wd = self.app.wd
        self.type("firstname", features_contact.firstname)
        self.type("middlename", features_contact.middlename)
        self.type("lastname", features_contact.lastname)
        self.type("nickname", features_contact.nickname)
        self.type("title", features_contact.title)
        self.type("company", features_contact.company)
        self.type("address", features_contact.address)
        self.type("home", features_contact.home)
        self.type("mobile", features_contact.mobile)
        self.type("work", features_contact.work)
        self.type("fax", features_contact.fax)
        self.type("email", features_contact.email)
        self.choice_group_contact(features_contact)

    def choice_group_contact(self, features_contact):
        wd = self.app.wd
        if features_contact.new_group is not None:
            # Выбираем группу для нового контакта
            wd.find_element_by_name("new_group").click()
            Select(wd.find_element_by_name("new_group")).select_by_visible_text(features_contact.new_group)
            wd.find_element_by_xpath(
                "//select[@name='new_group']/option[text()='" + features_contact.new_group + "']").click()
            wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()

    def type(self, field_name, text):
        wd = self.app.wd
        if field_name is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count_contact(self):
        wd = self.app.wd
        self.home_page(wd)
        return len(wd.find_elements_by_name("selected[]"))

    contacts_cache = None

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.home_page(wd)
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contacts_list(self):
        if self.contacts_cache is None:
            wd = self.app.wd
            self.home_page(wd)
            self.contacts_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text
                self.contacts_cache.append(FeaturesContact(firstname=firstname,
                                                           lastname=lastname,
                                                           id=id, all_phones_from_page=all_phones
                                                           ))
        return list(self.contacts_cache)

    def get_contact_info_from_edit_page(self,index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        return FeaturesContact(firstname=firstname, lastname=lastname, id=id, home=homephone, mobile=mobilephone, work=workphone)

    def get_contact_from_view_page(self,index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone=re.search("H: (.*)",text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        fax = re.search("F: (.*)", text).group(1)
        return FeaturesContact(home=homephone,
                               mobile=mobilephone,
                               work=workphone,
                               fax=fax)