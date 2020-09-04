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

