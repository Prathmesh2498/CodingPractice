# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 14:54:23 2020

@author: Admin
"""

Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:

Input: [1,2,3,4,5]
Output: true
Example 2:

Input: [5,4,3,2,1]
Output: false

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        min = float("inf")
        nextmin = float("inf")
        for i in range(len(nums)):
            if nums[i] < min:
                min = nums[i]
            elif nums[i] < nextmin and nums[i] > min:
                nextmin = nums[i]
            elif nums[i] > nextmin:
                return True
        return False