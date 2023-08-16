import time

from selenium.webdriver.common.by import By


class RequirmentPOM:
    __job_title_input_field_text="//*[@class='oxd-select-text-input']"
    __job_title_dropdown_xpath="//*[@class='oxd-select-dropdown --positon-bottom']/div"
    __job_title_dropdown_button_xpath="(//*[@class='oxd-select-text--after'])[1]"
    __vacancy_dropdown_button_xpath="(//*[@class='oxd-select-text--after'])[2]"
    __vacancy_dropdown_options_xpath="//*[@class='oxd-select-dropdown --positon-bottom']/div"
    __hiringManager_dropdown_button="(//*[@class='oxd-select-text--after'])[3]"
    __hiring_manager_dropdown_option_xpath="//*[@class='oxd-select-dropdown --positon-bottom']/div"
    __status_dropdown_button_xpath="(//*[@class='oxd-select-text--after'])[4]"
    __statu_dropdown_options_xpath="//*[@class='oxd-select-dropdown --positon-bottom']/div"


    def __init__(self,driver):
        self.driver=driver
    def validate_dropdown_default_name(self):
        return self.driver.find_element(By.XPATH,self.__job_title_input_field_text).text

    def job_title_dropdown_option_select(self,opt):
        # Get all options from the dropdown
        self.driver.find_element(By.XPATH,self.__job_title_dropdown_button_xpath).click()
        time.sleep((2))
        options = self.driver.find_elements(By.XPATH,self.__job_title_dropdown_xpath)
        for option in options:
            try:
             if option.text==opt:
                option.click()
            except Exception :
                print()

        time.sleep(1)


    def vacancy_dropdown_option_select(self,opt):
        # Get all options from the dropdown
        self.driver.find_element(By.XPATH,self.__vacancy_dropdown_button_xpath).click()
        time.sleep((2))
        options = self.driver.find_elements(By.XPATH,self.__vacancy_dropdown_options_xpath)
        for option in options:
            try:
                if option.text==opt:
                    option.click()
            except Exception :
                print()

        time.sleep(1)


    def hiringManager_dropdown_option_select(self,opt):
        # Get all options from the dropdown
        self.driver.find_element(By.XPATH,self.__hiringManager_dropdown_button).click()
        time.sleep((2))
        options = self.driver.find_elements(By.XPATH,self.__hiring_manager_dropdown_option_xpath)
        for option in options:
            print(option.text)
            try:
                if option.text==opt:
                    option.click()
            except Exception:
                print()

        time.sleep(1)


    def status_dropdown_option_select(self,opt):
        # Get all options from the dropdown
        self.driver.find_element(By.XPATH,self.__status_dropdown_button_xpath).click()
        time.sleep((2))
        options = self.driver.find_elements(By.XPATH,self.__statu_dropdown_options_xpath)
        for option in options:
            try:
                if option.text==opt:
                    option.click()
            except Exception:
                print()
        time.sleep(3)







