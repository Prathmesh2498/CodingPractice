# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 11:41:36 2020

@author: Admin
"""

#Heaps
import math
class Heap:
    def __init__(self):
        self.arr = []
        self.size = 0
        self.i = 1 #for one based indexing
        self.arr.insert(0,99999)
    
    def __str__(self):
        print(self.arr)
        return " "
     
    #__MAX_HEAP__        
    @staticmethod    
    def max_heapify(self,i):
        left = 2*i
        right = (2*i)+1
        largest = i
        if(left<=self.size  and self.arr[left]>self.arr[i]):
            largest = left
        elif(right<=self.size and self.arr[right]>self.arr[i]):
            largest = right
        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            Heap.max_heapify(self,largest)
    
            
    @staticmethod
    def heapify(self):
        for i in range(math.floor(self.size/2),0,-1):
            Heap.max_heapify(self,i)
            
    
    def add_toMaxHeap(self, element=None):
        if(element!=None):
            self.arr.insert(self.i, element)
            self.i+=1
            self.size = len(self.arr) - 1
            Heap.heapify(self)
            return
        raise NameError("Element not provided")
        
            
    #__MIN_HEAP__
    @staticmethod
    def min_Heapify(self, i):
        left = 2*i
        right = (2*i) + 1
        smallest = i
        if(left<=self.size  and self.arr[left]<self.arr[i]):
            smallest = left
        elif(right<=self.size  and self.arr[right]<self.arr[i]):
            smallest = right
        if(smallest!=i):
            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
            Heap.min_Heapify(self, smallest)
    
    
    @staticmethod
    def m_heapify(self):
        for i in range(math.floor(self.size/2),0,-1):
            Heap.min_Heapify(self,i)
    
    def add_toMinHeap(self, element = None):
        if(element!=None):
            self.arr.insert(self.i, element)
            self.i+=1
            self.size=len(self.arr) - 1
            Heap.m_heapify(self)
            return
        raise NameError("Element not provided")
    

#Main for Heap
h_min = Heap()
h_max = Heap()
l = [1,4,5,6,2]
#Call to Min Heap
for i in l:
    h_min.add_toMinHeap((i))
print(h_min)

#Call to Max Heap
for i in l:
    h_max.add_toMaxHeap((i))
print(h_max)
