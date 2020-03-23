#!/usr/bin/env python3
# -*- coding: utf-8 -*-
list_test = [x if x % 2 == 0 else -x for x in range(1, 11)]
print(list_test)
list_test = [x + 1 if x % 2 == 0 else -x for x in range(1, 11)]
print(list_test)
list_test = [x + 1 if x % 2 == 0 else -x for x in range(1, 20) if x % 3 == 0]
print(list_test)
print("测试中文")
print('zhu', 'xiao')
print('My name is %s ' % 'zhuxiaoshuai', 'What`s your name?')
