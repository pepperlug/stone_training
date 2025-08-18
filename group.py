#вспомогательный класс для создания новой группы
class Group:
    def __init__(self, name, header, footer):
        self.name = name
        self.header = header
        self.footer = footer
#вспомогательный класс для выбора группы в форме создания нового контакта
class ChangeGroup:
    def __init__(self, new_group):
        self.new_group = new_group