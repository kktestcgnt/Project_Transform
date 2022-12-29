import configparser
# import inspect
import time
import pytest
import logging
from datetime import datetime
from objects.app_login_page import LoginPageObjects

@pytest.mark.usefixtures("setup")
class BaseClass:

    def login(self):
        lp = LoginPageObjects(self.driver)
        lp.user_name().send_keys(self.get_data()['app_login_page']['user_id'])
        time.sleep(3)
        lp.user_password().send_keys(self.get_data()['app_login_page']['user_pwd'])
        time.sleep(3)
        lp.login_btn_action().click()
        time.sleep(3)

    # @staticmethod
    def get_data(self):
        data = configparser.ConfigParser()
        data.read("../data/data.ini")
        # data.read("E:/python_projects/Project_Transform/data/data.ini")
        print(data.sections())
        return data

    @staticmethod
    def logging():
        # Define Current time
        time_now = datetime.now()
        current_time = time_now.strftime("%d-%m-%Y--%H-%M-%S")

        # Define logger
        # name = inspect.stack()[1][3]
        logger = logging.getLogger(__name__)

        # Define new log level
        new_log_level = 60
        logging.addLevelName(new_log_level, "new_log_level")

        # Set log level
        logger.setLevel(logging.DEBUG)

        # Set Log Format
        formatter = logging.Formatter("%(asctime)s - %(filename)s - %(lineno)s - %(funcName)s - %(levelname)s - %$("
                                      "message)s")

        # Define File Handler
        file_handler = logging.FileHandler("../logs/log" + current_time + ".log", mode='a')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Define Console/Stream Handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        return logger

    def take_screenshot(self, image_name: "Add Extension to file name"):
        self.driver.save_screenshot("../screenshots/" + image_name)
