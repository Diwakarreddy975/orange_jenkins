from selenium.webdriver.common.by import By


class HomepagePOM:
    search_field_xpath="//*[@class='oxd-input oxd-input--active']"
    Admin_menu_xpath="//*[@class='oxd-main-menu']/li[1]"
    PIM_menu_xpath="//*[@class='oxd-main-menu']/li[2]"
    Leave_menu_xpath="//*[@class='oxd-main-menu']/li[3]"
    Requirtment_menu_xpath="//*[@class='oxd-main-menu']/li[5]"
    MY_INFO_menu_xpath="//*[@class='oxd-main-menu']/li[5]"
    Performance_menu_xpath="//*[@class='oxd-main-menu']/li[6]"
    Dashboard_menu_xpath="//*[@class='oxd-main-menu']/li[8]"
    Directory_menu_xpath="//*[@class='oxd-main-menu']/li[9]"
    Maintainance_menu_xpath="//*[@class='oxd-main-menu']/li[10]"
    claim_menu_xpath="//*[@class='oxd-main-menu']/li[11]"
    Bujj_menu_xpath="//*[@class='oxd-main-menu']/li[12]"
    user_dropdown_xpath="//span[@class='oxd-userdropdown-tab']"
    logout_xpath="//a[contains(text(),'Logout')]"


    def __init__(self,driver):
        self.driver=driver

    def click_on_user_dropdown(self):
        self.driver.find_element(By.XPATH,self.user_dropdown_xpath).click()

    def click_on_logout(self):
        self.driver.find_element(By.XPATH,self.logout_xpath).click()

    def user_drop_down_is_enabled(self):
        return self.driver.find_element(By.XPATH,self.user_dropdown_xpath).is_enabled()

    def click_Requirtment_menu(self):
        self.driver.find_element(By.XPATH,self.Requirtment_menu_xpath).click()


