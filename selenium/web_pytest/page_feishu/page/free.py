from selenium.webdriver.common.by import By

from page_feishu.page.basepage import Base

class Free(Base):
    def free(self):
        # self.driver.find_element_by_id('register_phone').send_keys('18888888888')
        #self.find(By.ID,'register_phone').send_keys('1888888888')
        self.keys(By.ID,'register_phone',1888888888)
        return self