import time

from common.common import BaseClass
from objects.app_login_page import LoginPageObjects


class TestLoginPageTests(BaseClass):

    def app_login(self):

        self.driver.implicitly_wait(3)
        lp = LoginPageObjects(self.driver)
        lp.user_name().send_keys(self.get_data()['app_login_page']['user_id'])
        # lp.user_name().send_keys(input("Enter Username: "))
        logger = self.logging()
        logger.info("Username entered successfully")
        logger.error("This is ERROR log")
        lp.user_password().send_keys(self.get_data()['app_login_page']['user_pwd'])
        # lp.user_password().send_keys(input("Enter Password: "))
        lp.login_btn_action().click()

        a = 10
        assert a == 8, ("Test Failed", logger.error("Test Failed"), self.take_screenshot("failed_image.png"))

    def test_app_login_page(self):
        self.app_login()
        self.driver.implicitly_wait(5)
        # time.sleep(5)








