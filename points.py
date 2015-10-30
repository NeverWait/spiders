# -*- coding:utf-8 -*-
import urllib
import json
import collections
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


# 一 易题库知识点格式
# 知识点分为三级：主知识点、一级子知识点、二级子知识点（有的没有该项）
# 知识点主要格式如下，有些在这个程序没有用的标签信息没有写出来
# <ul id="root">
#     <li>
#         <label bgid="一级子知识点编号">
#             <a>一级子知识点编号</a>
#         </label>
#         [ # 此括号内的数据为二级子知识点，有的li标签里面有这样的ul标签，而有的li标签里面没有这样的ul标签
#             <ul>
#                 <li>
#                     <label bgid="二级知识点编号">
#                         <a>二级知识点名</a>
#                     </label>
#                 </li>
#             </ul>
#         ]
#     </li>
#     ...
#     <li>
#     </li>
# </ul>
# 二 写入的json格式
# dd = {
#     '1': {
#         '主知识点': '多项式',
#         2: {
#             '一级子知识点名称': '一元多项式',
#             3: {
#                 '二级子知识点名称': '一元多项式求解'
#             }
#         }
#     }
# }
# 附：写入到txt的格式
# 知识点类别标示 知识点编号 知识点名字 一级知识点编号 主知识点编号
# 解释：知识点类别标示值为0、1、2，0表示主知识点；1为一级子知识点；2为二级子知识点

url = "http://www.yitiku.cn/tiku/shuxue/"
content = urllib.urlopen(url)
soup = BeautifulSoup(content, 'lxml')


url_root = soup.find(id="root")  # 取出包含所有知识点的ul标签


# li_list = url_root.contents
li_list = url_root.find_all('li', recursive=False)  # 求出ul下的一级li标签的个数
root_len = len(li_list)


point_dict = {}
# f = open('point.txt', 'w+')
for i in range(root_len):
    point_li = li_list[i]
    main_point = point_li.label.a.string  # 主知识点名称
    main_point_id = point_li.label['bgid']  # 主知识点编号

    # f.write('0' + ' ' + main_point_id + ' ' + main_point + '\n')  # 写入主知识点信息
    point_dict[main_point_id] = {'主知识点名称': main_point}

    child_ul_li = point_li.ul.find_all('li', recursive=False)  # 获取主li下的ul的所有li标签，该li标签子是知识点
    child_len = len(child_ul_li)
    for j in range(child_len):
        child_li = child_ul_li[j]
        first_child_level_name = child_li.a.string  # 一级子知识点名称
        first_child_level_id = child_li.label['bgid']  # 一级子知识点编号
        # f.write('1' + ' ' + first_child_level_id + ' ' +
        #         first_child_level_name + ' ' + '0' + ' ' + main_point_id + '\n')  # 写入一级子知识点
        point_dict[main_point_id][first_child_level_id] = {'一级子知识点名称': first_child_level_name}
        second_child_ul = child_li.ul  # 判断是否存在二级知识点
        if second_child_ul is not None:
            second_child_list = second_child_ul.find_all('li', recursive=False)  # 二级子知识点的list
            second_child_len = len(second_child_list)

            for k in range(second_child_len):
                second_child_name = second_child_list[k].a.string
                second_child_id = second_child_list[k].label['bgid']
                # f.write('2' + ' ' + second_child_id + ' ' +
                #         second_child_name + ' ' + first_child_level_id + ' ' + main_point_id + '\n')
                point_dict[main_point_id][first_child_level_id][second_child_id] = {'二级子知识点名称': second_child_name}

point_json = json.dumps(point_dict)

fj = open('point.json', 'w+')
fj.write(point_json)
fj.close()