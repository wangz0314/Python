# -*- coding: utf-8 -*-
#########################################################################
# File Name: read_lines_range.py
# Author: wangzhao
# mail:wangzhao314@126.com
# Created Time: 2015-06-23 20:23:19
#########################################################################
#!/usr/bin/python

'''read_lines_range.py start_line end_line'''

import sys

if __name__ == '__main__':
    start_line = int(sys.argv[1])
    end_line = int(sys.argv[2])

    data = open('data.txt', 'r')
    data_list = data.readlines()
    data.close()

    for line in data_list[start_line:end_line]:
        print line.strip()

