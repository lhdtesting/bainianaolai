from page.about_page import AboutPage
from page.address_list_page import AddressListPage
from page.be_vip_page import BeVipPage
from page.cart_page import CartPage
from page.category_page import CategoryPage
from page.edit_address_page import EditAddressPage
from page.good_detail_page import GoodDetailPage
from page.goods_list_page import GoodsListPage
from page.home_page import HomePage
from page.login_page import LoginPage
from page.person_center_page import PersonCenterPage
from page.register_page import RegisterPage
from page.search_page import SearchPage
from page.setting_page import SettingPage


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

    @property
    def get_setting_page_instance(self):
        return SettingPage(self.driver)

    @property
    def get_about_page_instance(self):
        return AboutPage(self.driver)

    @property
    def get_be_vip_instance(self):
        return BeVipPage(self.driver)

    @property
    def get_address_list_instance(self):
        return AddressListPage(self.driver)

    @property
    def get_edit_address_page_instance(self):
        return EditAddressPage(self.driver)

    @property
    def get_category_page_instance(self):
        return CategoryPage(self.driver)

    @property
    def get_goods_list_page_instance(self):
        return GoodsListPage(self.driver)

    @property
    def get_good_detail_page_instance(self):
        return GoodDetailPage(self.driver)

    @property
    def get_cart_page_instance(self):
        return CartPage(self.driver)

    @property
    def get_search_page_instance(self):
        return SearchPage(self.driver)


