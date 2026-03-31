from selenium.webdriver.support.ui import Select

class ContactHelper:
    def __init__(self,app):
        self.app = app

    #переход на форму создания нового контакта
    def form_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    # создание нового контакта
    def add_new_contact(self,features_contact):
        wd = self.app.wd
        self.form_contact()
        self.input_features_contact(features_contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()

    #обновление данных контакта
    def update_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    #удаление первого контакта в списке
    def del_first_contact(self):
        wd = self.app.wd
        #переход на форму существующих контактов
        self.home_page(wd)
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()

    #редактирование первого контакта в списке
    def edit_first_contact(self,features_contact):
        wd = self.app.wd
        #переход на форму существующих контактов
        self.home_page(wd)
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.input_features_contact(features_contact)
        self.update_contact()

    def home_page(self, wd):
        wd = self.app.wd
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
