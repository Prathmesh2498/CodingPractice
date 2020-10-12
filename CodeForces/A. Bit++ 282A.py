# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 23:31:41 2020
A. Bit++ 282A
@author: Admin
"""

n = int(input())

ans = 0
for i in range(n):
    arr = str(input())
    if arr[0] == '+' or arr[len(arr) - 1]=='+':
        ans += 1
    else:
        ans -= 1
print(ans)