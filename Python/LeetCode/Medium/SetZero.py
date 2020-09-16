# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 16:46:40 2020

@author: Admin
"""
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if (len(matrix)<=0):
            return
        flag = False
        flagRow = False
        flagCol = False

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    flag = True
                    if j == 0:
                        flagCol = True
                    if i == 0:
                        flagRow = True
                    matrix[0][j] = 0 
                    matrix[i][0] = 0
                    
        if flag == True:
            for j in range(len(matrix[0])):
                if (matrix[0][j] == 0 and flagCol != True and j==0):
                    continue
                if matrix[0][j] == 0:
                    for i in range(len(matrix)):
                        if (matrix[i][j]!= 0):
                            matrix[i][j] = float('inf')
            
            for j in range(len(matrix)):
                if (matrix[j][0] == 0 and flagRow != True and j==0):
                    continue
                if matrix[j][0] == 0:
                    for i in range(len(matrix[0])):
                        if (matrix[j][i]!= 0):
                            matrix[j][i] = float('inf')
            
            
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    if matrix[i][j] == float('inf'):
                        matrix[i][j] = 0
            
        return matrix