# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 11:40:48 2020

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