import time

from common.common import BaseClass
from objects.app_admin_page import AdminPageObjects
from objects.app_home_page import HomePageObjects



class TestAdminPage(BaseClass):

    def add_system_user(self):

        self.driver.implicitly_wait(3)
        obj_admin_page = AdminPageObjects(self.driver)
        logger = self.logging()

        obj_admin_page.su_add_btn_actn().click()
        logger.info("Clicked on Add tab in Admin Page successfully")
        time.sleep(10)

    def test_add_system_user(self):
        self.login()
        obj_home_page = HomePageObjects(self.driver)
        obj_home_page.hp_admin_page_tab_action().click()
        time.sleep(3)
        self.add_system_user()
