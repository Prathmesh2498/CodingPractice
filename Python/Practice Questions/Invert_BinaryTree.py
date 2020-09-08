# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 11:33:40 2020

@author: Admin
"""

class Tree:
    def __init__(self):
        self.head = None
        
        
    class Node:
        def __init__(self , data):
            self.data = data
            self.left = None
            self.right = None
            
    def __add(self, head, value):
        if(head is None):
            self.head = self.Node(value)
            return
        if(value < head.data):
            if(head.left is None):
                newNode = self.Node(value)
                head.left = newNode
            else:
                self.__add(head.left, value)
            
        elif(value > head.data):
             if(head.right is None):
                newNode = self.Node(value)
                head.right = newNode
             else:
                self.__add(head.right, value)
            
    def addNode(self, value):
        self.__add(self.head, value)
        
    def __inorder(self, head):
        if(head == None):
            return
        self.__inorder(head.left)
        print(head.data, end=" ")
        self.__inorder(head.right)
        
    def printInorder(self):
        self.__inorder(self.head)
        print()
        
        
    def __MirrorTree(self, head):
        if(head is None):
            return
        if (head.left is not None and head.right is None):
            head.right = head.left
            head.left = None
        elif (head.left is None and head.right is not None):
            head.left = head.right
            head.right = None
        elif (head.left is not None and head.right is not None):
            n = head.right
            head.right = head.left
            head.left = n
        self.__MirrorTree(head.left)
        self.__MirrorTree(head.right)
        
    def getMirror(self):
        self.__MirrorTree(self.head)
        
if __name__ == '__main__':
    t = Tree()
    n = [7,4,12,2,5,8,14,6,9]
    
    for i in n:
        t.addNode(i)
    t.printInorder()
    t.getMirror()
    t.printInorder()
        