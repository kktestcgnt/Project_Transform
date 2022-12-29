import time

from common.common import BaseClass
from objects.app_login_page import LoginPageObjects


class TestLoginPage(BaseClass):

    def app_login(self):

        self.driver.implicitly_wait(3)
        lp = LoginPageObjects(self.driver)
        lp.user_name().send_keys(self.get_data()['app_login_page']['user_id'])
        # lp.user_name().send_keys(input("Enter Username: "))
        logger = self.logging()
        logger.info("Username entered successfully")
        logger.error("This is ERROR log")
        time.sleep(3)
        lp.user_password().send_keys(self.get_data()['app_login_page']['user_pwd'])
        logger.info("Password entered successfully")
        time.sleep(3)
        # lp.user_password().send_keys(input("Enter Password: "))
        lp.login_btn_action().click()
        logger.info("Clicked on Login button successfully")
        time.sleep(3)

        # a = 10
        # assert a == 8, ("Test Failed", logger.error("Test Failed"), self.take_screenshot("failed_image.png"))
        #


    def test_login_page(self):
        self.app_login()
        self.driver.implicitly_wait(5)