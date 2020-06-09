# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 17:06:58 2020

@author: Admin
"""

class node:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = 0
        
    
                
class BinaryTree:
    def __init__(self, head):
        self.head = head
    
    @staticmethod 
    def inorderTraversal(head):
         if(head is None):
             return
         BinaryTree.inorderTraversal(head.left)
         print(head.data)
         BinaryTree.inorderTraversal(head.right)
        
    
    def addNode(self,head,data):
        
        if(head is None):
            print("Added in 1")
            head=node()
            head.data = data
            self.head = head
            return self.head
        elif (head.data>=data):
            if(head.left is None):
                print("Added in 2")
                head.left = node()
                head.left.data = data
                self.head = head
                return self.head
            else:
                self.addNode(head.left, data)
        elif(head.data<data):
            if(head.right is None):
                head.right = node()
                print("Added in 3")
                head.right.data = data
                self.head = head
                return self.head
            else:
                self.addNode(head.right, data)
                
     
                
    
                
                
if __name__ == '__main__':
    head = None
    tree = BinaryTree(head)
    n = int(input("Enter Number of nodes"))
    for i in range(0, n):
        t = int(input("Enter data: "))
        print()
        tree.head = tree.addNode(tree.head,t)
        print(tree.head.data)
        print("Added node {}".format(i+1))
    print("Printing inorder")
    BinaryTree.inorderTraversal(tree.head)
    
            