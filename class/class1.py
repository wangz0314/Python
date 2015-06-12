#########################################################################
# File Name: class.py
# Author: wangzhao
# mail:wangzhao314@126.com
# Created Time: 2015-06-12 17:08:48
#########################################################################
#!/usr/bin/python
# -*- coding: utf-8 -*-

class Person:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def greet(self):
        print "Hello,world! I'm %s." % self.name

wang = Person()
zhang = Person()

wang.setName('wangzhao')
zhang.setName('zhangxin')

wang.greet()
zhang.greet()
