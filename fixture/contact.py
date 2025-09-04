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
        wd.find_element_by_link_text("home").click()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()

    #редактирование первого контакта в списке
    def edit_first_contact(self,features_contact):
        wd = self.app.wd
        #переход на форму существующих контактов
        wd.find_element_by_link_text("home").click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.input_features_contact(features_contact)
        self.update_contact()
    #работа с атрибутами контакта
    def input_features_contact(self, features_contact,new_group=None):
        wd = self.app.wd
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
        if new_group is not None:
            # Выбираем группу для нового контакта
            wd.find_element_by_name("new_group").click()
            Select(wd.find_element_by_name("new_group")).select_by_visible_text(features_contact.new_group)
            wd.find_element_by_xpath(
                "//select[@name='new_group']/option[text()='" + features_contact.new_group + "']").click()
            wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
