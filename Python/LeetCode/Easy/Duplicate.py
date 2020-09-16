# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 16:53:14 2020

@author: Admin
"""

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true

class Solution:
    def containsDuplicate(self, a: List[int]) -> bool:
        check = {}
        for i in a:
            if i in check:
                return True
            else:
                check[i] = 1
        return False