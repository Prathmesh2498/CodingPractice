# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 11:22:10 2020

@author: Admin
"""

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum = 0
        d = -1
        c = 0
        l3 = None
        answer = None
        while (l1 or l2):
            sum=0
            if (l1 and l2):
                sum = l1.val + l2.val + c
            elif (l1):
                sum = l1.val + c
            elif (l2):
                sum = l2.val + c
            if (sum>=10):
                    d = sum%10
                    c = sum//10
            else:
                d = sum
                c = 0
            if(l3):
                l3.next = ListNode(d)
                l3 = l3.next
            else:
                l3 = ListNode(d)
                answer = l3
            if(l1):
                l1 = l1.next
            if(l2):
                l2 = l2.next
        if c!=0:
            l3.next = ListNode(c)
        return answer
        