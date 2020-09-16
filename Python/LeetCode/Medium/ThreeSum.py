# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 16:47:29 2020

@author: Admin
"""

iven an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if (len(nums)<3):
            return []
        nums.sort()
        res = []
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            l = i+1
            r = len(nums) - 1
            sum = 0 
            while(l<r):
                sum = a + nums[l] + nums[r]
                if (sum<0):
                    l += 1
                elif (sum>0):
                    r -= 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while(nums[l] == nums[l-1] and l<r):
                        l += 1
        return res
                    