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
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_header", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

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
        self.select_group(wd)
        wd.find_element_by_name("delete").click()
        self.return_to_groups()

    #редактирование данных первой в списке группы
    def edit_first_group(self, group):
        wd = self.app.wd
        self.open_groups()
        self.select_group(wd)
        wd.find_element_by_name("edit").click()
        self.input_group(group)
        self.update_group()
        self.return_to_groups()

    def select_group(self, wd):
        wd.find_element_by_name("selected[]").click()

    def count_group(self):
        wd = self.app.wd
        self.open_groups()
        return len(wd.find_elements_by_name("selected[]"))
