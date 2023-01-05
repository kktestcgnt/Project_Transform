from selenium.webdriver.common.by import By


class AdminPageObjects:

    def __init__(self, driver):
        self.driver = driver

    # 'au' tag is for the elements in Add User in Admin Page
    au_user_role = (By.XPATH, "//label[text() = 'User Role']//parent::div//following-sibling::div/div/div/div[1]")
    au_employee_name = (By.XPATH, "//label[text() = 'Employee Name']//parent::div//following-sibling::div/div/div/input")
    au_status = (By.XPATH, "//label[text() = 'Status']//parent::div//following-sibling::div/div/div/div[1]")
    au_username = (By.XPATH, "//label[text() = 'Username']//parent::div//following-sibling::div/input")
    au_password = (By.XPATH, "//label[text() = 'Password']//parent::div//following-sibling::div/input")
    au_confirm_password = (By.XPATH, "//label[text() = 'Confirm Password']//parent::div//following-sibling::div/input")
    au_cancel_btn = (By.XPATH, "//button[text() = ' Cancel ']")
    au_save_btn = (By.XPATH, "//button[text() = ' Save ']")

    # 'su' tag is for the elements in System Users search in Admin Page
    su_add_btn = (By.XPATH, "//button[text() = ' Add ']")
    su_username = (By.XPATH, "//label[text() = 'Username']//parent::div//following-sibling::div/input")
    # su_userrole = (By.XPATH, "//div[text() = '-- Select --']")
    su_user_role = (By.XPATH, "//label[text() = 'User Role']//parent::div//following-sibling::div/div/div/div[1]")
    su_user_role_admin = (By.XPATH, "//label[text() = 'User Role']//parent::div//following-sibling::div/div/div/div["
                                    "text() = 'Admin']")
    su_employee_name = (By.XPATH, "//input[@placeholder = 'Type for hints...']")
    su_status = (By.XPATH, "//label[text() = 'Status']//parent::div//following-sibling::div/div/div/div[1]")
    su_reset_btn = (By.XPATH, "//button[text() = ' Reset ']")
    su_search_btn = (By.XPATH, "//button[text() = ' Search ']")

    def au_user_role_actn(self):
        return self.driver.find_element(*AdminPageObjects.au_user_role)

    def au_employee_name_actn(self):
        return self.driver.find_element(*AdminPageObjects.au_employee_name)

    def au_status_actn(self):
        return self.driver.find_element(*AdminPageObjects.au_status)

    def au_username_actn(self):
        return self.driver.find_element(*AdminPageObjects.au_username)

    def au_password_actn(self):
        return self.driver.find_element(*AdminPageObjects.au_password)

    def au_confirm_password_actn(self):
        return self.driver.find_element(*AdminPageObjects.au_confirm_password)

    def su_add_btn_actn(self):
        return self.driver.find_element(*AdminPageObjects.su_add_btn)

    def su_employee_name_actn(self):
        return self.driver.find_element(*AdminPageObjects.su_employee_name)

