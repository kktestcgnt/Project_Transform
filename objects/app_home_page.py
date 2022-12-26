from selenium.webdriver.common.by import By


class HomePageObjects:

    def __init__(self, driver):
        self.driver = driver

    hp_admin_page_tab = (By.XPATH, "//span[text() = 'Admin']")

    def hp_admin_page_tab_action(self):
        return self.driver.find_element(*HomePageObjects.hp_admin_page_tab)
