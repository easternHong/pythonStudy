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


class Permission(Module):
    def __init__(self, gentle):
        self.name = None
        self.age = None
        self.__gentle = gentle

    def print_gentle(self):
        print('gentle:%s' % self.__gentle)


if __name__ == '__main__':
    module = Module('Chinese', 50)
    m = Module('Franch', 50)

    permission = Permission('man')
    permission.print_age()
    permission.print_gentle()

    # print("创建对象:" + module.__class__)
