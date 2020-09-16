# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 16:41:54 2020

@author: Admin
"""


Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if (len(s)>1000):
            return ""
        m = 0
        answer = ""
        for i in range(len(s)):
                l,r = i,i
                while (l>=0 and r<len(s) and s[l] == s[r]):
                    if m<r-l+1:
                        m = r-l+1
                        answer = s[l:r+1]
                    l -= 1
                    r += 1
                
                l,r = i,i+1
                while (l>=0 and r<len(s) and s[l] == s[r]):
                    if m<r-l+1:
                        m = r-l+1
                        answer = s[l:r+1]
                    l -= 1
                    r += 1
        return answer