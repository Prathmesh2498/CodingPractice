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
     
    @staticmethod
    def printLevelOrder(root): 
        # Base Case 
        if root is None: 
            return
          
        # Create an empty queue for level order traversal 
        queue = [] 
      
        # Enqueue Root and initialize height 
        queue.append(root) 
      
        while(len(queue) > 0): 
            # Print front of queue and remove it from queue 
            print (queue[0].data) 
            node = queue.pop(0) 
      
            #Enqueue left child 
            if node.left is not None: 
                queue.append(node.left) 
      
            # Enqueue right child 
            if node.right is not None: 
                queue.append(node.right) 
            
    def addNode(self,head,data):
        #For the first Node
        if(head is None):
            print("Added in 1")
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
                print("Added in 2")
                
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
                print("Added in 3")
               
            else:
                self.addNode(head.right, data)
                

def minval(head):
    if(head is None):
        return -1
    while(head.left!=None):
        head=head.left
    return head
            
# Given a binary search tree and a key, this function 
# delete the key and returns the new root 
def deleteNode(root, key): 
  
    # Base Case 
    if root is None: 
        return root  
  
    # If the key to be deleted is smaller than the root's 
    # key then it lies in  left subtree 
    if key < root.data: 
        root.left = deleteNode(root.left, key) 
  
    # If the kye to be delete is greater than the root's key 
    # then it lies in right subtree 
    elif(key > root.data): 
        root.right = deleteNode(root.right, key) 
  
    # If key is same as root's key, then this is the node 
    # to be deleted 
    else: 
          
        # Node with only one child or no child 
        if root.left is None : 
            temp = root.right  
            root = None 
            return temp  
              
        elif root.right is None : 
            temp = root.left  
            root = None
            return temp 
  
        # Node with two children: Get the inorder successor 
        # (smallest in the right subtree) 
        temp = minval(root.right) 
  
        # Copy the inorder successor's content to this node 
        root.data = temp.data
  
        # Delete the inorder successor 
        root.right = deleteNode(root.right , temp.data) 
  
  
    return root  
            
                
             
                
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
    #print("Printing preorder")
    #BinaryTree.preorderTraversal(tree.head)
    #print("Printing postorder")
    #BinaryTree.postorderTraversal(tree.head)
    tree.head = deleteNode(tree.head, 10)
    print(tree.head)
    BinaryTree.inorderTraversal(tree.head)    
            