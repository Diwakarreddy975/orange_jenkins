import time


from tests.pageclass.AdminPOM import Test_AdminPom
from tests.pageclass.homepagePOM import HomepagePOM
from tests.pageclass.loginpagePOM import LoginPOM
from tests.pageclass.requirtmentPOM import RequirmentPOM
from tests.testloggin import logs


class Test_Admin:
    def testadd_user(self):
        reqPOM = RequirmentPOM(self.driver)
        logpom = LoginPOM(self.driver)
        homepage = HomepagePOM(self.driver)
        logpom.enter_text_in_username("Admin")
        log=logs()
        log.loggingDemo().info("user enterd username")
        logpom.enter_password_in_password_field("admin123")
        log.loggingDemo().info("user enterd password")
        logpom.click_on_login_button()
        time.sleep(3)
        admin=Test_AdminPom(self.driver)
        admin.click_on_admin()
        log.loggingDemo().info("user clicked on admin")
        admin.click_add_button()
        log.loggingDemo().info("user clicked on add button")
        admin.password_sendkeys("diwakar@123")
        log.loggingDemo().info("user enterd password field")
        admin.confirm_password_send_keys("diwakar@123")
        log.loggingDemo().info("user enterd confirm password field")
        # admin.employee_sendkeys("Shihbs")

        admin.user_name_sendkeys("vasudha")
        log.loggingDemo().info("user enterd username field")

        admin.click_on_Status_dropdown()
        admin.click_status_dropdown_enable()
        log.loggingDemo().info("user selected enable option in status dropdown")
    def test_search_user_from_username_in_records_table(self):
        log = logs()
        reqPOM = RequirmentPOM(self.driver)
        logpom = LoginPOM(self.driver)
        homepage = HomepagePOM(self.driver)
        logpom.enter_text_in_username("Admin")
        logpom.enter_password_in_password_field("admin123")
        logpom.click_on_login_button()
        time.sleep(3)
        admin = Test_AdminPom(self.driver)
        admin.click_on_admin()
        admin.username_enter_search("Admin")
        log.loggingDemo().info("user enterd admin in search field")
        admin.search_button_click()
        time.sleep(5)
        admin.username_search_in_records("Admin")


    def test_search_user_from_status_in_records_table(self):
        reqPOM = RequirmentPOM(self.driver)
        logpom = LoginPOM(self.driver)
        homepage = HomepagePOM(self.driver)
        logpom.enter_text_in_username("Admin")
        logpom.enter_password_in_password_field("admin123")
        logpom.click_on_login_button()
        time.sleep(3)
        admin = Test_AdminPom(self.driver)
        admin.click_on_admin()
        admin.status_dropddown_search()
        admin.search_button_click()
        time.sleep(3)
        admin.status_search_in_records("Enabled")


    def test_delete_a_user(self):
        reqPOM = RequirmentPOM(self.driver)
        logpom = LoginPOM(self.driver)
        homepage = HomepagePOM(self.driver)
        logpom.enter_text_in_username("Admin")
        logpom.enter_password_in_password_field("admin123")
        logpom.click_on_login_button()
        time.sleep(3)
        admin = Test_AdminPom(self.driver)
        admin.click_on_admin()
        admin.delete_a_user()

