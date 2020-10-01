# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 12:43:55 2020

@author: Admin
"""

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
 

Constraints:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
The length of the linked list is between [0, 10^4].


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if(not head):
            return head
        if (not head.next):
            return head
        if (not head.next.next):
            return head
        
        odd = head
        even = head.next
        evenHead = even
        
        while(even is not None):
                odd.next = even.next
                if(odd.next is not None):
                    odd = odd.next
                    even.next = odd.next
                even = even.next
                
        
        odd.next = evenHead
        return head
        
        
        """
        count = 1
        
        first  = head.next
        second = head.next.next
        
        while(second):
            t = 0
            while(t<count):
                first.val, second.val = second.val, first.val
                t+=1
                if(t==1):
                    first = first.next
                    final = first
                else:
                    first = first.next
            first = final   
            if(second.next is None):
                second = second.next
            else:
                second = second.next.next
            count += 1
        return head
        """
        