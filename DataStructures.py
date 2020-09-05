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