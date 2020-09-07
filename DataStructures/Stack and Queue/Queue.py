# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 11:41:10 2020

@author: Admin
"""

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
