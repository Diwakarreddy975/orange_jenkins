import time
import random
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains

class Test_AdminPom:

    __admin_xpath="//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li"
    __add_button_xpath="//*[@class='orangehrm-header-container']/button"
    #user_role_dropdown_xpath="//*[@class='oxd-select-dropdown --positon-bottom']/div"
    __user_role_dropdown_xpath_ESS="//*[@class='oxd-select-dropdown --positon-bottom']/div"
    __status_dropdown_xpath_Enabled="//*[@class='oxd-select-dropdown --positon-bottom']/div[2]"

    __user_role_dropdown_xpath="(//*[@class='oxd-select-text--after'])[1]"
    __status_dropdown_xpath="(//*[@class='oxd-select-text--after'])[2]"
    __employee_name_xpath="//*[@class='oxd-autocomplete-wrapper']/div/input"
    __employee_dropdown_xpath="//*[@class='oxd-autocomplete-wrapper']/div[2]"
    __password_xpath="//*[@class='oxd-form-row user-password-row']/div/div/div/div[2]/input"
    __confirm_password_xpath="//*[@class='oxd-form-row user-password-row']/div/div[2]/div/div[2]/input"
    __user_name_xpath="(//*[@class='oxd-grid-item oxd-grid-item--gutters'])[4]/div/div[2]/input"
    __save_button_xpath="(//*[@class='oxd-form-actions'])/button[2]"
    __cancel_button_xpath="(//*[@class='oxd-form-actions'])/button[1]"
    __records_xpath="//*[@class='oxd-table-body']/div"
    __get_username_record_xpath="//*[@class='oxd-table-body']/div/div/div[2]"
    __username_search_xpath="(//*[@class='oxd-input-group oxd-input-field-bottom-space'])[1]/div[2]/input"
    __search_button_insearch_xpath="(//*[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space'])"
    __status_dropdown_search_xpath="(//*[@class='oxd-select-text oxd-select-text--active'])[2]"
    __status_enable_option_search_xpath="(//*[@class='oxd-select-dropdown --positon-bottom'])/div[2]"
    __get_status_record_xpath="//*[@class='oxd-table-body']/div/div/div[5]"
    __delete_button_in_records="//*[@class='oxd-icon-button oxd-table-cell-action-space']"
    __deleted_succesfully_notification="//*[@class='oxd-toast oxd-toast--success oxd-toast-container--toast']"
    __yes_delete_buttton="//*[@class='oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin']"
    def __init__(self,driver):
        self.driver=driver


    def click_on_admin(self):
        ele=self.driver.find_element(By.XPATH,self.__admin_xpath)
        ele.click()

    def click_add_button(self):
        self.driver.find_element(By.XPATH,self.__add_button_xpath).click()

    def click_on_user_role_dropdown(self):
        self.driver.find_element(By.XPATH,self.__user_role_dropdown_xpath).click()
        time.sleep(3)
        ele=self.driver.find_elements(By.XPATH,self.__user_role_dropdown_xpath_ESS)
        for e in ele:
            if e.text=="ESS":
                e.click()



    def click_on_Status_dropdown(self):
        self.driver.find_element(By.XPATH,self.__status_dropdown_xpath).click()


    def password_sendkeys(self,paswd):
        self.driver.find_element(By.XPATH, self.__password_xpath).send_keys(paswd)

    def confirm_password_send_keys(self,paswd):
        self.driver.find_element(By.XPATH, self.__confirm_password_xpath).send_keys(paswd)

    def user_name_sendkeys(self,user):
        self.driver.find_element(By.XPATH, self.__user_name_xpath).send_keys(user)

    def employee_sendkeys(self,emp_name):
        element=self.driver.find_element(By.XPATH, self.__employee_name_xpath)
        element.send_keys(emp_name)




    def save_button_click(self):
        self.driver.find_element(By.XPATH, self.__save_button_xpath)

    def check_username_in_records(self,username):
        ele=self.driver.find_elements(By.XPATH, self.__records_xpath)
        for e in ele:
            if e==username:
                print("found")
                assert True
            else:
                assert False

    def click_status_dropdown_enable(self):
        self.driver.find_element(By.XPATH, self.__status_dropdown_xpath_Enabled).click()


    def username_enter_search(self,username):
        self.driver.find_element(By.XPATH,self.__username_search_xpath).send_keys(username)

    def search_button_click(self):
        self.driver.find_element(By.XPATH, self.__search_button_insearch_xpath).click()

    def username_search_in_records(self,username):
        ele=self.driver.find_elements(By.XPATH, self.__get_username_record_xpath)
        for e in ele:
            print(e.text)
            if e.text==username:
             assert True

    def status_dropddown_search(self):
        self.driver.find_element(By.XPATH,self.__status_dropdown_search_xpath).click()
        self.driver.find_element(By.XPATH,self.__status_enable_option_search_xpath).click()

    def status_search_in_records(self, username):
        ele = self.driver.find_elements(By.XPATH, self.__get_status_record_xpath)
        for e in ele:
            print(e.text)
            if e.text == username:
                assert True
            else:
                assert False



    def delete_a_user(self):
        ele = self.driver.find_elements(By.XPATH, self.__get_username_record_xpath)
        print(ele)
        l = []
        global username
        for e in ele:
            print(e.text)
            l.append(e.text)

            username = random.choice(l)

        self.driver.find_element(By.XPATH, self.__username_search_xpath).send_keys(username)
        self.driver.find_element(By.XPATH, self.__search_button_insearch_xpath).click()
        time.sleep(3)
        username = random.choice(l)
        self.driver.find_element(By.XPATH, self.__delete_button_in_records).click()



        time.sleep(3)
        self.driver.find_element(By.XPATH,self.__yes_delete_buttton).click()
        time.sleep(2)
        ele=self.driver.find_element(By.XPATH,self.__deleted_succesfully_notification)
        if ele.is_displayed():
            assert True
        else:
            assert False













