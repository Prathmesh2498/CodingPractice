# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 10:46:44 2020

@author: Admin
"""

#Stack
class stack:
   def __init__(self):
       self.size = 0
       self.st = [] 
       
   def pop(self):
       if(self.size>0):
           element = self.st.pop()
           self.size = len(self.st)
           return element
       raise NameError("Stack Empty") 
       
   def push(self, element=None):
        if(element!=None):
            self.st.append(element)
            self.size = len(self.st)
            return
        raise NameError("Element not provided")
        
   def top(self):
       if(self.size>0):
           return self.st[-1]
       raise NameError("Stack is Empty")
   
#Main for stack
stk = stack()
for i in range(0,5):
    stk.push(i)
print(stk.top())
stk.pop()
print(stk.top())

#Queue
class queue:
   def __init__(self):
       self.size = 0
       self.st = [] 
       
   def dequeue(self):
       if(self.size>0):
           element = self.st.pop(0)
           self.size = len(self.st)
           return element
       raise NameError("Queue Empty") 
       
   def enqueue(self, element=None):
        if(element!=None):
            self.st.append(element)
            self.size = len(self.st)
            return
        raise NameError("Element not provided")
        
   def front(self):
       if(self.size>0):
           return self.st[0]
       raise NameError("Queue is Empty")
       
#Main for Queue
q = queue()
for i in range(0,5):
    q.enqueue(i)
print(q.front())
print("Dequeue: {}".format(q.dequeue()))
print(q.front())

#Priority Queue
class queue:
   def __init__(self):
       self.size = 0
       self.st = {} 
   
   def __str__(self):
        print(self.st)
        return " "
         
   def dequeue(self):
       if(self.size>0):
           index = min(self.st,key=self.st.get)
           element = self.st[index]
           del self.st[index]
           self.size = len(self.st)
           return element
       raise NameError("Queue Empty") 
       
   def enqueue(self, element=None, priority = -1):
        if(element!=None):
            self.st[priority] = element
            self.size = len(self.st)
            return
        raise NameError("Element not provided")
        
   def max_priority(self):
       if(self.size>0):
           index = min(self.st,key=self.st.get)
           return self.st[index]
       raise NameError("Queue is Empty")

#Main for Priority Queue       
q = queue()
for i in range(6,11):
    q.enqueue(i, i-5)
print(q)
print(q.max_priority())
print("Dequeue: {}".format(q.dequeue()))
print(q.max_priority())

"""
NOTE:
    A way to convert min pq to a max pq, just negate the priority values.
"""

#Heaps
import math
class Heap:
    def __init__(self):
        self.arr = []
        self.size = 0
        self.i = 1
        self.arr.insert(0,99999)
    
    def __str__(self):
        print(self.arr)
        return " "
     
    #__MAX_HEAP__        
    @staticmethod    
    def max_heapify(self,i):
        left = 2*i
        right = 2* (i+1)
        largest = i
        if(left<=self.size - 1 and self.arr[left]>self.arr[i]):
            largest = left
        elif(right<=self.size - 1 and self.arr[right]>self.arr[i]):
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
            self.size = len(self.arr)
            Heap.heapify(self)
            return
        raise NameError("Element not provided")
        
            
    #__MIN_HEAP__
    @staticmethod
    def min_Heapify(self, i):
        left = 2*i
        right = 2*(i+1)
        smallest = i
        if(left<=self.size - 1 and self.arr[left]<self.arr[i]):
            smallest = left
        elif(right<=self.size - 1 and self.arr[right]<self.arr[i]):
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
            self.arr.insert(i, element)
            self.i+=1
            self.size=len(self.arr)
            Heap.m_heapify(self)
            #As we don't count index 0, th e value there messes things up in recursive call
            self.arr[0], self.arr[self.size-1] = self.arr[self.size-1], self.arr[0] 
            return
        raise NameError("Element not provided")
    

#Main for Heap
h = Heap()

#Call to Min Heap
for i in range (0,5):
    c = int(input("Enter Number: "))
    h.add_toMinHeap(c)
    print(h)

#Call to Max Heap
for i in range (0,5):
    c = int(input("Enter Number: "))
    h.add_toMaxHeap(c)
    print(h)

