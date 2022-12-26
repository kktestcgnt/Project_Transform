import time

from common.common import BaseClass
from tests.test_app_login_page import TestLoginPageTests
from objects.app_home_page import HomePageObjects


class TestHomePageTests(TestLoginPageTests):

    def go_to_admin_page(self):

        self.driver.implicitly_wait(3)
        obj_home_page = HomePageObjects(self.driver)
        logger = self.logging()

        obj_home_page.hp_admin_page_tab_action().click()
        logger.info("Clicked on Admin tab in Home Page successfully")
        time.sleep(3)

    def go_to_admin_page_tests(self):
        self.app_login_page()
        self.go_to_admin_page()

    def test_go_to_admin_page(self):
        self.go_to_admin_page_tests()
