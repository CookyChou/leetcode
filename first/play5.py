#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/4 17:24
# @Author  : bgzhou
def containsDuplicate(nums):
    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         if nums[i] == nums[j]:
    #             return True
    # return False

    return len(nums) != len(set(nums))


if __name__ == '__main__':
    list1 = [1, 2, 2, 4, 5]
    print(containsDuplicate(list1))