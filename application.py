from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class Application:
    def __init__(self):
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        self.wd = webdriver.Firefox(executable_path=r'C:\Windows\SysWOW64\geckodriver.exe', options=options)
        self.wd.implicitly_wait(30)
    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def return_to_groups(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def submit_new_group(self):
        wd = self.wd
        wd.find_element_by_name("submit").click()

    def add_new_group(self, group):
        wd = self.wd
        self.open_groups()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        self.submit_new_group()
        self.return_to_groups()
    def open_groups(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def login(self, user, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
    def destroy(self):
        self.wd.quit()

    def add_new_contact(self, features_contact):
        #вводим фио и никнейм нового контакта
        wd = self.wd
        self.form_new_contact()
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
        # Выбираем группу для нового контакта
        wd.find_element_by_name("new_group").click()
        Select(wd.find_element_by_name("new_group")).select_by_visible_text(features_contact.new_group)
        wd.find_element_by_xpath("//select[@name='new_group']/option[text()='" + features_contact.new_group + "']").click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()

    def form_new_contact(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()