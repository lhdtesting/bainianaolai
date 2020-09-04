from time import sleep

from base.base_driver import init_driver


class TestLogin:

    def setup(self):
        self.driver = init_driver()

    def teardown(self):
        sleep(2)
        self.driver.quit()

    def test_login(self):
        print("test_login")