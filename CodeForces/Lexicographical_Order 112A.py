# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 23:42:50 2020
Lexicographical_Order 112A
@author: Admin
"""

n1  = str(input()).lower()
n2  = str(input()).lower()

if n1 == n2:
    print(0)
    
else:
    index1 = -1
    index2 = -1
    cnt1 = 0
    cnt2 = 0
    for i,j in zip(n1, n2):
        index1 += 1
        index2 += 1
        if i == j:
            continue
        else:
            if ord(i) > ord(j):
                print(1)
            else:
                print(-1)
            break

"""
Test Casess
bwuEhEveouaTECagLZiqmUdxEmhRSOzMauJRWLQMppZOumxhAmwuGeDIkvkBLvMXwUoFmpAfDprBcFtEwOULcZWRQhcTbTbX
HhoDWbcxwiMnCNexOsKsujLiSGcLllXOkRSbnOzThAjnnliLYFFmsYkOfpTxRNEfBsoUHfoLTiqAINRPxWRqrTJhgfkKcDOH
"""