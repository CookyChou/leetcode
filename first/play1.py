#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/4 11:46
# @Author  : bgzhou


class Solution:
    def removeDuplicates(self, nums):
        # for i in nums:
        #     for j in nums[nums.index(i)+1:]:
        #         if i == j:
        #             nums.remove(j)
        # return len(nums)
        if len(nums) == 0:
            return
        i = 0
        for j in range(len(nums)):
            if nums[i] != nums[j]:
                i = i + 1
                nums[i] = nums[j]
        return i+1


if __name__ == '__main__':
        s = Solution()
        list1 = [1, 1, 1, 2, 2, 3]
        print(s.removeDuplicates(list1))
        print(list1)