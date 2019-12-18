# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 13:36:36 2019
8.10 Paint Fill
@author: Priya Mehta
"""

class area:
    def __init__(self, val: list):
        self.colors = val
    
    def print_area(self):
        for row in self.colors:
            for col in row:
                print(col, end="")
            print()
    
    def paint_fill(self,point: tuple, new_color: int):
        (row, col) = point
        old_color = self.colors[row][col]
        
        def rec(point: tuple):
            nonlocal old_color
            nonlocal new_color
            (row, col) = point
            if self.colors[row][col] != old_color:
                return
            self.colors[row][col] = new_color
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    new_row = row + i
                    new_col = col + j 
                    if new_row >= 0 and new_row <len(self.colors) and new_col >= 0 and new_col < len(self.colors[0]):
                        rec((new_row, new_col))
        rec(point)
                
# Driver Code
l= [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,1,1,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0],
          [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
          [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
          [0,0,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0],
          [0,0,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0],
          [0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,1,0,0,0,0],
          [0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0],
          [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
          [0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

A = area(l)
A.print_area()
A.paint_fill((0,0), 5)
print()
A.print_area()