# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 16:56:02 2020

@author: Admin
"""

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
Example 3:

Input: matrix = [[1]]
Output: [[1]]
Example 4:

Input: matrix = [[1,2],[3,4]]
Output: [[3,1],[4,2]]
 

Constraints:

matrix.length == n
matrix[i].length == n
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        """
        #Flip Diagonally:
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if (i != j and i<=j):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        #Flip Horizontally
        for i in range(len(matrix)):
            t = len(matrix[i]) - 1
            for j in range(int(len(matrix)/2)):
                if (j<t):
                    matrix[i][j], matrix[i][t] = matrix[i][t], matrix[i][j]
                t-=1