# -*- coding:utf-8 -*-
import json
from StringIO import StringIO

f_json = open('yitiku_points_name.json', 'r+')
point_str = f_json.read()
point_io = StringIO(point_str)
point_dict = json.load(point_io)

for name in point_dict:
    if name in point_dict[name]:
        print name
    for f_name in point_dict[name]:
        if f_name in point_dict[name][f_name]:
            print f_name
            print name
        for s_name in point_dict[name][f_name]:
            if s_name in point_dict[name]:
                print s_name
