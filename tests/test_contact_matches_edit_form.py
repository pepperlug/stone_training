import re

def test_info_on_home_page(app):
    # Получаем контакт с главной страницы
    contact_from_home_page = app.contact.get_contacts_list()[0]
    # Получаем данные этого же контакта со страницы редактирования
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    #проверяем что данные совпадают: имя, фамилия, адрес, емейлы и телефоны
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_email_from_page == merge_email_like_on_home_page(contact_from_edit_page)

def test_phone_on_contact_view_page(app):
    # Получаем контакт со страницы просмотра
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    # Получаем полные данные контакта со страницы редактирования
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    #сравниваем телефоны
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.work == contact_from_edit_page.work

def clear_phone(s):
    # Удаляем скобки, пробелы и дефисы из строки
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(features_contact):
    # Склеиваем все телефоны в строку, как они отображаются на главной странице
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_phone(x),
                                filter(lambda x: x is not None,
                                       [features_contact.home,
                                        features_contact.mobile,
                                        features_contact.work]))))

def merge_email_like_on_home_page(features_contact):
    # Склеиваем все е-мейлы в строку, как они отображаются на главной странице
    return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None,
                                       [features_contact.email,
                                        features_contact.email2,
                                        features_contact.email3])))