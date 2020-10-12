# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 22:31:06 2020

@author: Admin

A. Way Too Long Words
71-A
"""

n = int(input())
for i in range(n):
    s = str(input())
    p = len(s)
    if p>10:
        print(s[0]+str(p-2)+s[p-1])
    else:
        print(s)
    
    

