# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 12:55:03 2020

@author: Admin
"""

#Union Find

class uFind:
    def __init__(self):
        self.arr = []
        self.size = []
        self.num_components
        
    def init_input(self, arr):
        self.arr = arr
        self.size = [1] * len(arr)
        self.num_components = len(arr)
        
    def num_components(self):
        return self.num_components
        
    def connected(self, p, q):
        if (self.arr[p] == self.arr[q]):
            return True
        return False
    
    def find(self, p):
        root = p
        while(self.arr[root]!=root):
            root = self.arr[root]
        
        #Path Compression
        while(p!=root):
            t=self.arr[p]
            self.arr[p] = root
            p = t
        
        return root
    
    def union(self, p, q):
        
        root1 = self.find(p)
        root2 = self.find(q)
        #First check if p and q are already in same component
        if(root1 == root2):
            return
        
        if (self.size[root1]<=self.size[root2]):
            self.size[root2]+=self.size[root1]
            self.arr[root1] = root2
        else:
            self.size[root1]+=self.size[root2]
            self.arr[root2] = root1
            
        self.num_components-=1
        
            
#Main for Union Find
u = uFind()

arr = [i for i in range(0,5)]

u.init_input(arr)
print(u.num_components)#5
u.union(0,1)
print(u.num_components)#4
u.union(1,0)
print(u.num_components)#4
u.union(1,2)
print(u.num_components)#3
u.union(0,2)
print(u.num_components)#3
u.union(2,1)
print(u.num_components)#3
u.union(3,4)
print(u.num_components)#2
u.union(4,3)
print(u.num_components)#2
u.union(1,3)
print(u.num_components)#1
u.union(4,0)
print(u.num_components)#1
