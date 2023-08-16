import time

import selenium
from selenium.webdriver.common.by import By


class LoginPOM:
    username_name = "username"
    password_name = 'password'
    login_xpath = "//button[@type='submit']"
    forgot_password_xpath = "//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']"
    orange_hrm_logo_xpath="//*[@id='app']/div[1]/div/div[1]/div/div[1]/img"
    invalid_credentials_warning="//div[@role='alert']"
    user_field_warning_msg_xpath="//*[@name='username']/parent::div/following-sibling::span"
    passw_field_warning_msg_xpath="//*[@name='password']/parent::div/following-sibling::span"

    def __init__(self, driver):
        self.driver = driver

    def enter_text_in_username(self, text):
        self.driver.find_element(By.NAME,self.username_name).send_keys(text)

    def enter_password_in_password_field(self,password):
        password_field=self.driver.find_element(By.NAME,self.password_name)
        password_field.send_keys(password)

    def click_on_forgot_password(self):
        self.driver.find_element(By.XPATH,self.forgot_password_xpath).click()

    def click_on_login_button(self):
        self.driver.find_element(By.XPATH,self.login_xpath).click()

    def is_logo_displayed(self):
        self.driver.find_element(By.XPATH,self.orange_hrm_logo_xpath).is_displayed()

    def login_page_title_validation(self,title):
        assert self.driver.title==title

    def invalid_credential_alert(self,invalid):
        assert self.driver.find_element(By.XPATH,self.invalid_credentials_warning).text==invalid

    def user_warning_field(self):
        return self.driver.find_element(By.XPATH,self.user_field_warning_msg_xpath).text

    def pasw_warning_field(self):
        return self.driver.find_element(By.XPATH,self.passw_field_warning_msg_xpath).text

    def password_masking_validation(self,password):
        webele=self.driver.find_element(By.NAME,self.password_name)
        webele.send_keys(password)
        return webele.get_attribute("type")







