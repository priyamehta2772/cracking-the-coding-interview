# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 16:43:33 2019

@author: priya
Rotate matrix by 90 degrees
"""

def rotate90(matrix: list) -> list:
    if not matrix:
        return matrix
    dim = len(matrix)
    #transpose in place
    for r in range(dim):
        for c in range(r,dim):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
    #mirror image of cols
    for r in range(dim):
        for c in range( int(dim/2) ):
            matrix[r][c], matrix[r][dim-1-c] = matrix[r][dim-1-c], matrix[r][c]
    return matrix

matrix1 = [[1,2,3], [4,5,6], [7,8,9]]
matrix2 = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
matrix3 = [[1,2], [3,4]]
print(rotate90(matrix2))