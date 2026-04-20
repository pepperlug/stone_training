from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from fixture.contact import ContactHelper
from fixture.session import SessionHelper
from fixture.groups import GroupHelper

class Application:
    def __init__(self,browser="firefox"):
        if browser == "firefox":
            options = Options()
            options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
            self.wd = webdriver.Firefox(executable_path=r'C:\Windows\SysWOW64\geckodriver.exe', options=options)
        elif browser == "chrome":
            self.wd = webdriver.Chrome(executable_path=r"C:\path\to\chromedriver.exe")
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" + browser)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
    def destroy(self):
        self.wd.quit()
