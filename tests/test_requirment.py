import time

from tests.pageclass.requirtmentPOM import RequirmentPOM
from tests.pageclass.loginpagePOM import LoginPOM
from tests.pageclass.homepagePOM import HomepagePOM

class Test_Requirment:
    def test_validating_dropdown_for_default_name(self):
        reqPOM=RequirmentPOM(self.driver)
        logpom = LoginPOM(self.driver)
        homepage = HomepagePOM(self.driver)
        logpom.enter_text_in_username("Admin")
        logpom.enter_password_in_password_field("admin123")
        logpom.click_on_login_button()
        time.sleep(3)
        homepage.click_Requirtment_menu()
        assert reqPOM.validate_dropdown_default_name()=="-- Select --"

    def test_getoptions(self):
        reqPOM = RequirmentPOM(self.driver)
        logpom = LoginPOM(self.driver)
        homepage = HomepagePOM(self.driver)
        logpom.enter_text_in_username("Admin")
        logpom.enter_password_in_password_field("admin123")
        logpom.click_on_login_button()
        time.sleep(3)
        homepage.click_Requirtment_menu()
        reqPOM.job_title_dropdown_option_select("HR Manager")
        reqPOM.vacancy_dropdown_option_select("Sales Representative")
        reqPOM.hiringManager_dropdown_option_select("Dominic Chase")
        reqPOM.status_dropdown_option_select("Job Offered")



