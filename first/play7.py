#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/8 14:30
# @Author  : bgzhou
from collections import Counter

def intersect(nums1, nums2):
    result = []
    for i in nums1:
        for j in range(len(nums2)):
            if i == nums2[j]:
                result.append(i)
                nums2.remove(nums2[j])
                break
    return result

    # 比较快的解法
    # return list((Counter(list1) & Counter(list2)).elements())


if __name__ == '__main__':
    list1 = [1, 2, 2, 1]
    list2 = [2, 2]
    print(Counter(list1))
    print(Counter(list2))
    print(list((Counter(list1) & Counter(list2)).elements()))