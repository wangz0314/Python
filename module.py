#########################################################################
# File Name: modu2.py
# Author: wangzhao
# mail:wangzhao314@126.com
# Created Time: 2015-06-06 10:43:48
#########################################################################
#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import sys 

print( time.asctime() )
print '------------------------------------'
print 'Please input your age(int, 0->exit):'
age = int( sys.stdin.readline() )
while True:
    if age > 18 and age < 40: 
        print('you are young')
    elif age == 18: 
        print('you are 18')
    elif age < 18 and age > 0:
        print('you are a child')
    elif age == 0:
        print 'exit'
        break
    else:
        print('you are a older')
    print '------------------------------------'
    print 'Please input your age(int, 0->exit):'
    age = int( sys.stdin.readline() )
