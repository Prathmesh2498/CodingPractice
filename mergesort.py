# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 12:00:19 2020

@author: Admin
"""


"""
Time Complexity: O(nlogn)
Stable 
Not inplace in usual implementation
Auxilary Space: O(n)
"""

def mergeSort(arr): 
  
    if len(arr)>1: 
        m = len(arr)//2
        left = arr[:m] 
        right = arr[m:] 
        left = mergeSort(left) 
        right = mergeSort(right) 
  
        arr =[] 
  
        while len(left)>0 and len(right)>0: 
            if left[0]<right[0]: 
                arr.append(left[0]) 
                left.pop(0) 
            else: 
                arr.append(right[0]) 
                right.pop(0) 
  
        for i in left: 
            arr.append(i) 
        for i in right: 
            arr.append(i) 
                  
    return arr 


li = [4,6,7,8,9,5,3,1,2,10]
li = mergeSort(li)
for e in li:
    print(e)
        