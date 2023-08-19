import pytest
from selenium import webdriver
from allure_commons.types import AttachmentType
import allure

@pytest.fixture(autouse=True)
def setup(request):
    driver=webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.implicitly_wait(10)
    request.cls.driver=driver
    yield
    allure.attach(driver.get_screenshot_as_png(), name=f"{request.node.name}_screenshot",
                          attachment_type=AttachmentType.PNG)
    driver.close()
