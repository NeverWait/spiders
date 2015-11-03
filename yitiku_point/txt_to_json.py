# -*- coding:utf-8 -*-
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 改文件的作业是把chao.txt中的知识点转化为json格式。
# 1、先从chaos.txt取出名字和浮点数
# 2、将其转化为dict，然后转化为json
# 3、从易题库中一次取出json值，将其权重置为0或者相应的值

f = open('chaos.txt', 'r')

num = 0
point_dict = {}
while 1:
    lines = f.readlines(500)
    if not lines:
        break
    for line in lines:
        part_list = line.split(' ', 1)
        point_dict[part_list[0].decode('gbk')] = float(part_list[1][:-1])
        num += 1
# print num  # num的值为137
f = open('weight.json', 'w+')
f.write(json.dumps(point_dict))
f.close()

