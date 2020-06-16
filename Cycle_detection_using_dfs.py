# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 15:54:56 2020

@author: Admin
"""
from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.Vertices = vertices
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
        
    def detectCycle(self, v, visited, rec):
        visited[v] = True
        rec[v] = True

        for n in self.graph[v]:
            if visited[n]==False:
                if self.detectCycle(n, visited, rec) == True:
                    return True
            elif rec[n] == True:
                return True
        rec[v] = False
        return False
    
    def callDetect(self):
        visited = [False] * self.Vertices
        rec = [False] * self.Vertices
        for node in range(self.Vertices):
            if visited[node] == False:
                if(self.detectCycle(node, visited, rec)==True):
                    return True
        return False
  
if __name__ == '__main__':
    g = Graph(4) 
    g.addEdge(0, 1) 
    g.addEdge(0, 2) 
    g.addEdge(1, 2) 
    g.addEdge(2, 0) 
    g.addEdge(2, 3) 
    g.addEdge(3, 3) 
    if g.callDetect() == True: 
        print("Graph has a cycle")
    else: 
        print("Graph has no cycle")      