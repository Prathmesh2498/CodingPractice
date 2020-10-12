# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 22:44:28 2020
A. Team - 231A
@author: Admin
"""


n = int(input())
ans = 0
for i in range(n):
    arr = list(map(int, input().rstrip().split()))
    if arr.count(1) >= 2:
       ans += 1
print(ans)
            
