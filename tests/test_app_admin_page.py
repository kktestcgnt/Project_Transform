import time

from common.common import BaseClass
from objects.app_admin_page import AdminPageObjects

from tests.test_app_login_page import TestLoginPageTests
from tests.test_app_home_page import TestHomePageTests


class TestAdminPageTests(TestHomePageTests):

    def add_system_user(self):

        self.driver.implicitly_wait(3)
        obj_admin_page = AdminPageObjects(self.driver)
        logger = self.logging()

        obj_admin_page.su_add_btn_actn().click()
        logger.info("Clicked on Add tab in Admin Page successfully")
        time.sleep(50)

    def test_add_system_user(self):
        self.go_to_admin_page_tests()
        self.add_system_user()
