#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'test_module'
__author__ = 'eastern'

import sys


# 读取命令行输入参数
def func():
    args = sys.argv
    if len(args) == 1:
        print('参数个数:1->%s' % args[0])
    elif len(args) == 2:
        print('参数个数:2->%s,%s' % (args[0], args[1]))


if __name__ == '__main__':
    print('模块使用')
    func()
