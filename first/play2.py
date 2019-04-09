#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/4 14:04
# @Author  : bgzhou


class Solution:
    def removeElement(self, nums, val):
        if len(nums) == 0:
            return
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i


if __name__ == '__main__':
    s = Solution()
    list1 = [1, 1, 2, 3]
    print(s.removeElement(list1, 2))
    print(list1)
