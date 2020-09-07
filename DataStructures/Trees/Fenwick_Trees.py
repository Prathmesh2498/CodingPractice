# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 12:55:27 2020

@author: Admin
"""

#Fenwick Trees
class Fenwick:
    def __init__(self, arr):
        self.tree = arr
        self.build_Ftree()
        
        
    def lsb(self, x):
        return x & -x
    
    def build_Ftree(self):
        for i in range(1,len(self.tree)):
            j = i + self.lsb(i)
            if(j<len(self.tree)):
                self.tree[j] += self.tree[i]
    
    def prefixSum(self, i):
        sum=0
        while(i!=0):
            sum+=self.tree[i]
            i -= self.lsb(i)
        return sum
            
    def sumRange(self, i, j):
        if (j<i):
            raise NameError("J cannot be less than I")
        else:
            return self.prefixSum(j) - self.prefixSum(i-1)#Why i-1?
    
    def pointUpdate(self, index, valueToAdd):
        while(index<len(self.tree)):
            self.tree[index] += valueToAdd
            index += self.lsb(index)

#Main for Fenwick Trees
f = Fenwick([99,1,2,3,4,5,6])
print(f.sumRange(1,6))