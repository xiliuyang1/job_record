import time

import pytest
import yaml

from page.base_data import data_file
from page.index import Index

class Test_index:
    def setup(self):
        self.index=Index()

    #参数化
    @pytest.mark.parametrize('phone,pwd,ver,status',yaml.safe_load(open('../data/data.yml','r')))
    def test_login(self,phone,pwd,ver,status):
        self.index.goto_login().login(phone,pwd,ver)
        # 判断是否登录成功
        if status == 'True':
            try:

                time.sleep(3)
                assert True,self.index.goto_login().page_if_login_success()
                print('登录成功')


            except:
                self.index.base_get_image()
                time.sleep(8)

            self.index.goto_login().page_exit()



        else:
            self.index.base_get_image()

    # def test_shop(self):
    #     self.index.goto_shop().shop()

 # 直接传参数
 #    @pytest.mark.parametrize('keyword',['电视','小米'])
 #    def test_shop(self,keyword):
 #        self.index.goto_shop(keyword).shop()


# 外部文件传参数
#     @pytest.mark.parametrize('args',data_file())
#     def test_shop(self,args):
#         keyword = args['keyword']
#         self.index.goto_shop(keyword).shop()


#
# 灵活传输
    @pytest.mark.parametrize('args',data_file('search_data.yaml','test_search'))
    def test_shop(self,args):
        keyword = args['keyword']
        self.index.goto_shop(keyword).shop()
        assert '添加成功',self.index.goto_shop(keyword).shop_add()
        print('添加成功')















