# index  页面  进行case组装
import pytest
import yaml

from page_feishu.page.index import Index

class Test_Index:
    # 初始化
    def setup(self):
        self.index = Index()


    def test_login(self):
        self.index.goto_login().login().free()


    # @pytest.mark.parametrize('phone',yaml.safe_load(open('../data/data.yaml','rb')))
    # def test_free(self,phone):
    #     self.index.goto_free().free(phone=phone)
    def test_free(self):
        self.index.goto_free().free()
    def teardown(self):
        self.index.close()