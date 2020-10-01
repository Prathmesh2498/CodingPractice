# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 12:00:55 2020

@author: Admin
"""
 
def getZero(a):
    return a[0]

import math
def solve(x,a):
    answer = []
    li =[]
    for i in range(len(a)):
        li.append([math.ceil(a[i]/x),i])
    li.sort(key=getZero)
    for x in li: 
          answer.append(x[1]+1) 
    return answer
        


a = []
T = int(input())
for i in range(T):
    _,x = map(int, input().strip().split())
    a =  list((map(int, input().strip().split())))
    p = solve(x,a)
    print("Case #{}: {}".format(i+1, ' '.join(map(str, p))), end= '\n')



