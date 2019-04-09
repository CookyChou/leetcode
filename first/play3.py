#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/4 15:15
# @Author  : bgzhou


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        j = 0
        length1 = len(haystack)
        length2 = len(needle)
        if length2 == 0:
            return 0
        for i in range(length1):
            if haystack[i] == needle[0]:
                if (length1-i) < length2:
                    return -1
                else:
                    j = i
                    t = True
                    for k in range(1, len(needle)):
                        if haystack[i+k] != needle[k]:
                            t = False
                    if t:
                        return j
                    else:
                        continue
        return -1

    def strStr1(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        i = 0
        j = 0
        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                j += 1
                i += 1
            else:
                i = i - j + 1
                j = 0
        if j == len(needle):
            return i - j
        return -1


if __name__ == '__main__':
    str1 = "mississippi"
    s = Solution()
    print(s.strStr(str1, "issip"))