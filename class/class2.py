# -*- coding: utf-8 -*-
########################################################################
# File Name: class2.py
# Author: wangzhao
# mail:wangzhao314@126.com
# Created Time: 2015-06-12 17:58:13
########################################################################
#!/usr/bin/python

'类的继承与使用；当使用多超类继承时，先继承的类中的方法会重写后继承类中的方法'

class Counter:
    def count(self, expression):
        self.value = eval(expression)
        print 'Counter类的count()方法!'
    def user(self):
        print "Hi, Counter's value is", self.value
        print "Counter类的user()方法!"

class User:
    def user(self):
        print "Hi, User's value is", self.value
        print "User类的user()方法!"

class New1(Counter, User):
    pass                            #先继承Counter类

class New2(User, Counter):
    pass                            #先继承User类

print 'uc1=New1(Counter, User)的结果:'
print 

uc1 = New1()                        #将使用Counter类的user()方法
uc1.count('1+2*3')
uc1.user()
print

print '------------------------------'

print 'uc2=New2(User, Counter)的结果:'
print

uc2 = New2()                        #将使用User类的user()方法
uc2.count('2+3*6')
uc2.user()
print

