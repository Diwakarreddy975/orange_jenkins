import time

from tests.pageclass.loginpagePOM import LoginPOM
from tests.pageclass.forgotpagePOM import forgotPagePOM
from tests.pageclass.homepagePOM import HomepagePOM



class Test_loginpage:
    def test_login_with_valid_credentials(self):

        logpom = LoginPOM(self.driver)  # Use 'self.driver' to access the 'driver' instance
        logpom.enter_text_in_username("Admin")
        logpom.enter_password_in_password_field("admin123")
        logpom.click_on_login_button()
        assert self.driver.title == "OrangeHRM"  # Use 'self.driver' here as well

    def test_login_with_invalid_credentials(self):

        logpom = LoginPOM(self.driver)  # Use 'self.driver' to access the 'driver' instance
        logpom.enter_text_in_username("username")
        logpom.enter_password_in_password_field("admin123")
        logpom.click_on_login_button()
        logpom.invalid_credential_alert("Invalid credentials")

    def test_clicking_login_with_out_entering_user_pass_fields(self):
        logpom = LoginPOM(self.driver)
        logpom.click_on_login_button()
        assert logpom.user_warning_field()=="Required"
        assert logpom.pasw_warning_field()=="Required"

    def testlogo_validation_on_login_page(self):
        logpom = LoginPOM(self.driver)
        logpom.is_logo_displayed()

    def test_password_masking(self):
        logpom = LoginPOM(self.driver)
        assert logpom.password_masking_validation("admin123")=="password", "password is not masked"

    def test_forgot_password_validation(self):
        logpom = LoginPOM(self.driver)
        reset_password_page=forgotPagePOM(self.driver)
        logpom.click_on_forgot_password()
        reset_password_page.enter_username("Admin")
        reset_password_page.click_on_Reset_password()
        assert reset_password_page.resetpassword_link_success()=="Reset Password link sent successfully"


    def test_logout_validation(self):
        logpom = LoginPOM(self.driver)
        homepage=HomepagePOM(self.driver)
        logpom.enter_text_in_username("Admin")
        logpom.enter_password_in_password_field("admin123")
        logpom.click_on_login_button()
        homepage.click_on_user_dropdown()
        time.sleep(3)
        homepage.click_on_logout()
        time.sleep(3)
        self.driver.back()
        time.sleep(4)
        assert False ==homepage.user_drop_down_is_enabled()





















