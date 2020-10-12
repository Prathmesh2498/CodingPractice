# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 23:05:07 2020
A. Next Round 158-A
@author: Admin
"""


n =   list(map(int, input().rstrip().split())) 
arr = list(map(int, input().rstrip().split()))
 
i = 0
ans = 0 
while(i<n[0] and arr[i]>=arr[n[1] - 1]):
    if arr[i] != 0:
        ans += 1
    i+=1
print(ans)