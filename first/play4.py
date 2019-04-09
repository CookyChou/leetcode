#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/4 16:38
# @Author  : bgzhou
class Solution:
    def rotate(self, nums, k: int) -> None:
        nums[:] = nums[-(k % len(nums)):] + nums[:-(k % len(nums))]


if __name__ == '__main__':
    s = Solution()
    list1 = [1, 2]
    s.rotate(list1, 3)
    print(list1)