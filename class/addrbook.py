# -*- coding: utf-8 -*-
#########################################################################
# File Name: addrbook.py
# Author: wangzhao
# mail:wangzhao314@126.com
# Created Time: 2015-06-12 21:53:55
#########################################################################
#!/usr/bin/python

class Addrbook:
    'address book class'
    def __init__(self, nm, ph):
        self.name = nm
        self.phone = ph
        print 'Created record for:', self.name
    
    def updatephone(self, newph):
        self.phone = newph
        print 'Update phone for:', self.name

class EmplyAddrbook(Addrbook):
    'employ address book class'
    def __init__(self, nm, ph, id, em):
        Addrbook.__init__(self, nm, ph)             #不是通过实例调用Addrbook的__init__(),未绑定的方法调用需要传递self给方法
        self.id = id
        self.email = em

    def updateEmail(self, newem):
        self.email = newem
        print 'Update the email for:', self.name

wang = EmplyAddrbook('wangzhao', '123456', 0001, 'wangzhao@126.com')
print 'wang.name :', wang.name
print 'wang.phone :', wang.phone
print 'wang.email :', wang.email

phone = raw_input('Please input new phone num:')
wang.updatephone(phone)                             #使用父类的updatephone方法
print 'wang.phone :', wang.phone

email = raw_input('Please input new email:')
wang.updateEmail(email)                             #使用自己的updateEmail方法
print 'wang.email :', wang.email
