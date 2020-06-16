# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 13:50:42 2020

@author: Admin
"""
from collections import defaultdict 
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
        #self.graph[v].append(u)
        
    def dfs(self, node, visited):
        if(visited[node] == True):
            return
        visited[node] = True
        print(node)
        
        for i in self.graph[node]:
            if(visited[i]!=True):
                self.dfs(i,visited)
        
    def dfsCall(self, start, no_of_nodes):
        visited = [False] * (no_of_nodes)
        self.dfs(start, visited)
        
    def bfs(self, node, no_of_nodes):
        visited = [False] * (no_of_nodes)
        
        queue = []
        queue.append(node)
        visited[node]=True
        while len(queue)>0:
            s = queue.pop(0)
            print(s)
            for i in self.graph[s]:
                if(visited[i]==False):
                    visited[i]=True
                    queue.append(i)
       
        
if __name__ == '__main__':
    n=int(input("No of nodes: "))    
    g = Graph() 
    g.addEdge(0, 1) 
    g.addEdge(0, 2) 
    g.addEdge(1, 2) 
    g.addEdge(2, 0) 
    g.addEdge(2, 3) 
    g.addEdge(3, 3) 
      
    print ("Following is Breadth First Traversal"
                      " (starting from vertex 2)") 
    g.bfs(2,n) 