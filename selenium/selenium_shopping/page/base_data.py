import os

import yaml

#
# def data_file():
#     with open('../data/search_data.yaml','r',encoding='utf-8') as f:
#         case_data = yaml.safe_load(f)
#         # 创建空列表 ， 数据加进来
#         data_list = list()
#         # 首先提取第一层key值   再提取字典对应values值
#         for i in case_data['test_search'].values():
#             data_list.append(i)
#         return data_list
#
# print(data_file())



# 灵活处理方法

def data_file(filename,key):
    with open('..%sdata%s%s'%(os.sep,os.sep,filename),'r',encoding='utf-8') as f:
        case_data = yaml.safe_load(f)[key]
        # 创建空列表 ， 数据加进来
        data_list = list()
        # 首先提取第一层key值   再提取字典对应values值
        for i in case_data.values():
            data_list.append(i)
        return data_list


