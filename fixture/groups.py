class GroupHelper:

    def __init__(self, app):
        self.app = app

    #переход в раздел групп
    def open_groups(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    #переход в форму создания новой группы
    def click_new_group(self):
        wd = self.app.wd
        wd.find_element_by_name("new").click()

    #ввод данных создаваемой либо редактируемой группы
    def input_group(self,group):
        wd = self.app.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
    #метод создания новой группы
    def create(self, group):
        wd = self.app.wd
        self.open_groups()
        self.click_new_group()
        self.input_group(group)
        self.submit_new_group()
        self.return_to_groups()

    #подтверждение создания нвоой группы
    def submit_new_group(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    #подтверждение обновления данных группы
    def update_group(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    #возврат к списку существующих групп
    def return_to_groups(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    #метод удаления первой группы в списке
    def del_first_group(self):
        wd = self.app.wd
        self.open_groups()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("delete").click()
        self.return_to_groups()

    #редактирование данных первой в списке группы
    def edit_first_group(self, group):
        wd = self.app.wd
        self.open_groups()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        self.input_group(group)
        self.update_group()
        self.return_to_groups()
