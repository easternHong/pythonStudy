#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 面向对象

# 括号中的object,表示Module类继承自object
class Module(object):
    # __init__函数的第一个参数永远是self
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print('name is :%s' % self.name)

    def print_age(self):
        print('age is :%s' % self.age)


if __name__ == '__main__':
    module = Module('Chinese', 50)
    m = Module('Franch', 50)
    m.good = 9
    m.good
    module.good

    # print("创建对象:" + module.__class__)
