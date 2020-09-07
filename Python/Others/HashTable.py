# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 12:55:12 2020

@author: Admin
"""

#Hashtable - Open Addressing: Separate Chaining
class hashTable:
    def __init__(self, size=10):
        self.size = size
        self.keys = [-1] * size
        self.value = [[None for i in  range(0,1)] for j in range(size)]
        #self.ldf = 0.5 #Load Factor Not needed as list auto expand
        #self.threshold = self.size * self.key
        
    def computeHash(self, key):
        return key%10
        
    def addValue(self, value):
        index = self.computeHash(value)
        if(self.keys[index] == -1):
            self.keys[index] = index
        self.value[index].append(value)
        if(None in self.value[index]):
            self.value[index].remove(None)
    
    def __str__(self):
        for i in self.keys:
            s = str(i) + ": " + str(self.value[i])
            print(s)
        return " "
    
    def searchValue(self, value):
        index = self.computeHash(value)
        if(self.keys[index] == -1):
            return "Value Absent"
        elif(value in self.value[index]):
            return "Element Present"
        return "Element Absent"
    
#Main For HashTable
h = hashTable()
for i in range(1, 13):
    h.addValue(i)
print(h)
h.searchValue(100)
h.searchValue(11)