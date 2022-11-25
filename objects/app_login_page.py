from selenium.webdriver.common.by import By


class LoginPageObjects:

    def __init__(self, driver):
        self.driver = driver

    username = (By.XPATH, "//input[@name = 'username']")
    password = (By.XPATH, "//input[@name = 'password']")
    login_btn = (By.XPATH, "//button[text() = ' Login ']")

    def user_name(self):
        return self.driver.find_element(*LoginPageObjects.username)

    def user_password(self):
        return self.driver.find_element(*LoginPageObjects.password)

    def login_btn_action(self):
        return self.driver.find_element(*LoginPageObjects. login_btn)

