# -*- coding:utf-8 -*-
import json
from StringIO import StringIO

# 1、依次读出yitiku.json的key，查找在weight.json中是否存在
# 2、如果存在的话将它的权重值设为相应的float；
# 3、计算权重，由内向外，一级子知识点的权重等于他所有二级的和，主知识点的权重等于他的所有一级子知识点的和
# 4、备注

f_weight = open('weight.json', 'r')
weight_str = f_weight.read()
weight_io = StringIO(weight_str)
weight_dict = json.load(weight_io)


f_json = open('yitiku_points_name.json', 'r+')
point_str = f_json.read()
point_io = StringIO(point_str)
point_dict = json.load(point_io)

num = 0  # 记录修改的行数，无实际作用

#  将知识点的权重对应到weight.json上面
for root_name in point_dict:
    for first_child_name in point_dict[root_name]:
        if first_child_name in weight_dict:
            if first_child_name not in point_dict[root_name][first_child_name]:
                point_dict[root_name][first_child_name][u'权重'] = weight_dict[first_child_name]
                num += 1
        # print first_child_name
        if first_child_name != u'权重' and first_child_name != u'主知识点编号':
            first_child_len = len(point_dict[root_name][first_child_name])
            if first_child_len > 2:
                for sec_child_name in point_dict[root_name][first_child_name]:
                    if sec_child_name in weight_dict:
                        point_dict[root_name][first_child_name][sec_child_name][u'权重'] = weight_dict[sec_child_name]
                        num += 1

#  算出一级子知识点的权重
for r_name in point_dict:
    for f_c_name in point_dict[r_name]:
        if f_c_name != u'主知识点编号' and f_c_name != u'权重' and len(point_dict[r_name][f_c_name]) > 2:
            for s_c_name in point_dict[r_name][f_c_name]:
                if s_c_name != u'一级子知识点编号' and s_c_name != u'权重':
                    point_dict[r_name][f_c_name][u'权重'] += point_dict[r_name][f_c_name][s_c_name][u'权重']

#  算出总知识点的权重
for root_name in point_dict:
    for first_child_name in point_dict[root_name]:
        if first_child_name != u'权重' and first_child_name != u'主知识点编号':
            point_dict[root_name][u'权重'] += point_dict[root_name][first_child_name][u'权重']

#  测试看所有主知识点的权重的和是不是为100
# total = 0.0
# for root_name in point_dict:
#     total += point_dict[root_name][u'权重']
# print total  # 返回值为105.053050398
#  print num  # num值为138，该值应该和txt_to_json的num（137）值是一样的，未找到错误原因
f = open('yitiku_points_weight.json', 'w+')
f.write(json.dumps(point_dict))
f.close()
