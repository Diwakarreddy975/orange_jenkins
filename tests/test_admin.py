import time

from tests.pageclass.AdminPOM import Test_AdminPom
from tests.pageclass.homepagePOM import HomepagePOM
from tests.pageclass.loginpagePOM import LoginPOM
from tests.pageclass.requirtmentPOM import RequirmentPOM


class Test_Admin:
    def testadd_user(self):
        reqPOM = RequirmentPOM(self.driver)
        logpom = LoginPOM(self.driver)
        homepage = HomepagePOM(self.driver)
        logpom.enter_text_in_username("Admin")
        logpom.enter_password_in_password_field("admin123")
        logpom.click_on_login_button()
        time.sleep(3)
        admin=Test_AdminPom(self.driver)
        admin.click_on_admin()
        admin.click_add_button()
        admin.password_sendkeys("diwakar@123")
        admin.confirm_password_send_keys("diwakar@123")
        # admin.employee_sendkeys("Shihbs")

        admin.user_name_sendkeys("vasudha")

        admin.click_on_Status_dropdown()
        admin.click_status_dropdown_enable()

        admin.click_on_user_role_dropdown()

        admin.save_button_click()
        time.sleep(5)