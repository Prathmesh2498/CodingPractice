# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 16:03:33 2020

@author: Admin
"""

class AVLRecursive:
    def __init__(self):
        self.head = None
        self.num_of_nodes = 0
        
    pass #EndFun
        
    class node:            
        def __init__(self, value):
            self.left = None
            self.right = None
            self.data = value
            self.balance_factor = 0
            self.height = 0
    
    pass #EndInnerClass
            
    def __leftRotate(self, node):
        newParent = node.right
        node.right = newParent.left
        newParent.left = node
        self.__update(node)
        self.__update(newParent)
        return newParent
    pass #EndFun    
    
    def __rightRotate(self, node):
        newParent = node.left
        node.left = newParent.right
        newParent.right = node
        self.__update(node)
        self.__update(newParent)
        return newParent
    pass #EndFun    
    
    def __leftRightRotate(self, node):
        node = self.__leftRotate(node)
        return self.__rightRotate(node)
    pass #EndFun
    
    def __rightLeftRotate(self, node):
        node = self.__rightRotate(node)
        return self.__leftRotate(node)
    pass #EndFun
    
    def __update(self, node):
        lh = -1 if node.left == None else node.left.height
        rh = -1 if node.right == None else node.right.height
       
        node.height = 1 + max(lh,rh)
        
        bf = rh - lh
        
        return bf
    pass #EndFun
        
                
    def __insertNode(self, node, value):
        if (node==None):
            return self.node(value)
       
        if(value<node.data):
            node.left = self.__insertNode(node.left, value)
        
        elif(value>node.data):
            node.right = self.__insertNode(node.right, value)
            
        node.balance_factor = self.__update(node)
        return self.__balance(node)
    pass #EndFun
    
    def __balance(self,node):
        if (node.balance_factor == -2):
            if(node.left.balance_factor<=0):
                #Left-Left Case
                return self.__rightRotate(node)
            else:
                #left-Right Case
                return self.__leftRightRotate(node)
        if (node.balance_factor == +2):
            if(node.right.balance_factor>=0):
                #Right-Right Case
                return self.__leftRotate(node)
            else:
                #Right-Left Case
                return self.__rightLeftRotate(node)
        return node
    pass #EndFun
   
    
    def __contains(self, value):
        if(self.head.data == value):
            return True
        node = self.head
        temp = 0
        while(node!=None):
            if(node.data == value):
                temp = 1
                break
            if(value < node.data):
                node = node.left
            else:
                node = node.right
        if(temp==1):
            return True
        return False
    pass #EndFun
    
    def __minval(head):
        if(head is None):
            return -1
        while(head.left!=None):
            head=head.left
        return head
    pass #EndFun
    
    def __remove(self,node,value):
        if(node==None):
            return node
        if(value < node.data):
                node = node.left
        elif(value>node.data):
                node = node.right
        else:
            if (node.left==None):
                temp = node.right
                node = None
                return temp
            elif (node.right==None):
                temp=node.left
                node=None
                return temp
            else:
                temp = self.__minval(node)
                node.data = temp.data
                node = self.__remove(node.right, temp.data)
        
        node.balance_factor = self.__update(node)
        return self.__balance(node)
    pass #EndFun
    
    #Public Functions
    def insert(self,value):
        self.head  = self.__insertNode(self.head,value)
    pass #EndFun
        
    def delete(self, value):
        self.head = self.__remove(self.head,value)
    pass #EndFun
        
            
#Main for AVL
a = AVLRecursive()
a.insert(1)
print(a.head.data)
a.insert(2)
a.insert(3)
print(a.head.data)