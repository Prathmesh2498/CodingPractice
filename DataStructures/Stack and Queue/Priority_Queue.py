# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 11:41:24 2020

@author: Admin
"""

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