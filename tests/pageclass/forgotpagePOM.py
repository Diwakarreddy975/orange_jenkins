from selenium.webdriver.common.by import By
# jhgsgyujma


class forgotPagePOM:
    forgor_password_title_xpath="//h6[@class='oxd-text oxd-text--h6 orangehrm-forgot-password-title']"
    user_xpath="//input[@name='username']"
    cancel_xpath="//button[@class='oxd-button oxd-button--large oxd-button--ghost orangehrm-forgot-password-button orangehrm-forgot-password-button--cancel']"
    reset_password_button_xpath="//button[@class='oxd-button oxd-button--large oxd-button--secondary orangehrm-forgot-password-button orangehrm-forgot-password-button--reset']"
    reset_password_succesful_link_xpath="//h6[@class='oxd-text oxd-text--h6 orangehrm-forgot-password-title']"
    def __init__(self,driver):
        self.driver=driver


    def enter_username(self,username):
        self.driver.find_element(By.XPATH,self.user_xpath).send_keys(username)

    def click_on_Reset_password(self):
        self.driver.find_element(By.XPATH,self.reset_password_button_xpath).click()

    def Click_on_cancel(self):
        self.driver.find_element(By.XPATH,self.cancel_xpath).click()

    def resetpassword_link_success(self):
        return self.driver.find_element(By.XPATH,self.reset_password_succesful_link_xpath).text
