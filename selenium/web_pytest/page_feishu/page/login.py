from selenium.webdriver.common.by import By

from page_feishu.page.basepage import Base

from page_feishu.page.free import Free
import time
class Login(Base):
    def login(self):
        self.driver.find_element_by_xpath('//div[@class="login-go-registe"]/span/span').click()

        # self.click(By.XPATH,'//div[@class="login-go-registe"]/span/span')
        return Free(self.driver)