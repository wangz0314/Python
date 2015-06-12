#########################################################################
# File Name: dic.py
# Author: wangzhao
# mail:wangzhao314@126.com
# Created Time: 2015-06-11 21:44:10
#########################################################################
#!/usr/bin/python
# -*- coding: utf-8 -*-

people = {
    'wang':{
        'phone':'1234',
        'addr':'addr first'
        },
    'zhang':{
        'phone':'6782',
        'addr':'addr second'
        },
    'huang':{
        'phone':'8910',
        'addr':'addr third'
        }
    }

lable = {
    'phone':'phone number',
    'addr':'address'
    }

name = raw_input('Name:')

if name in people:
    request = raw_input('Phone number (p) or address (a)?')
#    assert request, 'don\'t have the people'
else:
    print "don't have the people"
    exit()

if request == 'p':
    key = 'phone'
if request == 'a':
    key = 'addr'
#if name in people:
print "%s's %s is %s." % (name, lable[key], people[name][key])


