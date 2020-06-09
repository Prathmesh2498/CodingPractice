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
         
    @staticmethod
    def preorderTraversal(head):
         if(head is None):
             return
         print(head.data)
         BinaryTree.preorderTraversal(head.left)
         BinaryTree.preorderTraversal(head.right)
         
         
    @staticmethod
    def postorderTraversal(head):
         if(head is None):
             return
         BinaryTree.postorderTraversal(head.left)
         BinaryTree.postorderTraversal(head.right)
         print(head.data)
            
    def addNode(self,head,data):
        #For the first Node
        if(head is None):
            #print("Added in 1")
            #Create a New Node
            newnode=node()
            newnode.data = data
            self.head = newnode
            
        
        #For adding left nodes
        elif (head.data>=data):
            if(head.left is None):
                #Create a New Node
                newnode = node()
                newnode.data = data
                #Add the NewNode
                head.left = newnode
                #print("Added in 2")
                
            else:
                self.addNode(head.left, data)
        
        #For adding right nodes
        elif(head.data<data):
            if(head.right is None):
                #Create a New Node
                newnode = node()
                newnode.data = data
                #Add node
                head.right = newnode
                #print("Added in 3")
               
            else:
                self.addNode(self.head.right, data)
                
                
if __name__ == '__main__':
    head = None
    tree = BinaryTree(head)
    n = int(input("Enter Number of nodes"))
    for i in range(0, n):
        t = int(input("Enter data: "))
        print()
        tree.addNode(tree.head,t)
    print("Printing inorder")
    BinaryTree.inorderTraversal(tree.head)
    print("Printing preorder")
    BinaryTree.preorderTraversal(tree.head)
    print("Printing postorder")
    BinaryTree.postorderTraversal(tree.head)
    
            