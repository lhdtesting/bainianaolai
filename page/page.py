from page.home_page import HomePage
from page.login_page import LoginPage
from page.person_center_page import PersonCenterPage
from page.register_page import RegisterPage


class Page:
    def __init__(self, driver):
        self.driver = driver

    @property
    def get_home_page_instance(self):
        return HomePage(self.driver)

    @property
    def get_login_page_instance(self):
        return LoginPage(self.driver)

    @property
    def get_register_page_instance(self):
        return RegisterPage(self.driver)

    @property
    def get_person_center_page_instance(self):
        return PersonCenterPage(self.driver)

