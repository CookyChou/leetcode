#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/4 17:45
# @Author  : bgzhou

def singleNumber(nums: list):
    k = 0
    for i in nums:
        k = k ^ i
    return k

if __name__ == '__main__':
    print(singleNumber([1, 2, 2, 1, 3]))