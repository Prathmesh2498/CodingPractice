# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 16:53:48 2020

@author: Admin
"""

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        limit = len(nums)
        for i in range(0,limit):
            single = nums[0]
            nums.pop(0)
            if (single not in nums):
                break
            else:
                nums.append(single)
        return single
