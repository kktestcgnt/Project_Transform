
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service

from common.common import BaseClass

driver = None


class DataExtractor(BaseClass):

    @classmethod
    def data_extractor(cls):
        data = BaseClass.get_data(cls)['app_login_page']['app_url']
        return data


@pytest.fixture(autouse=True, params=[DataExtractor.data_extractor()])
def setup(request):

    global driver
    obj_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=obj_service)
    # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.maximize_window()
    print(request.param)
    driver.get(request.param)
    driver.implicitly_wait(15)

    request.cls.driver = driver
