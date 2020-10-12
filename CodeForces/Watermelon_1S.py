# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 18:52:53 2020

@author: Admin

Watermelon 4A
"""

n = int(input())

if n<=100 and n>=1:
    if (n-2)%2 == 0 and n-2>0:
        print("YES")
    else:
        print("NO")