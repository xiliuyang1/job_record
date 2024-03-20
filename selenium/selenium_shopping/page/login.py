from selenium.webdriver.common.by import By

from page.base import Base

class Login(Base):
    def login(self,phone,pwd,ver):
        # self.driver.find_element_by_id('username').send_keys('18888888888')
        self.input(By.ID,'username',phone)
        # self.driver.find_element_by_id('password').send_keys('123456')
        self.input(By.ID,'password',pwd)
        # self.driver.find_element_by_id('verify_code').send_keys('8888')
        self.input(By.ID,'verify_code',ver)
        # self.driver.find_element_by_name('sbtbutton').click()
        self.click(By.NAME,'sbtbutton')

    def page_if_login_success(self):
        return self.base_element_is_exist(self.find(By.LINK_TEXT,'安全退出'))


    def page_exit(self):
        return self.driver.find_element(By.LINK_TEXT,'安全退出').click()