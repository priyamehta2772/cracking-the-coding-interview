# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 18:08:07 2019

@author: priya
Stack of boxes
"""

class box:
    def __init__(self, h, w, d):
        self.height = h
        self.width  = w
        self.depth  = d
        
    def hasLargerWidth(self, b2) -> bool:
        return True if (self.width>b2.width) else False
        
    def hasLargerDepth(self, b2) -> bool:
        return True if (self.depth>b2.depth) else False
    
class StackOfBox:
    def __init__(self, allBoxes):
        self.maxHeight = 0
        self.boxes = allBoxes
    
    def printBoxes(self):
        print("\nBoxes: ", end="")
        for b in self.boxes:
            print(" (", end="")
            print(b.height, b.width, b.depth, sep="," ,end = "")
            print(")", end="") 
    
    # do a merge sort here with help of nested functions
    def sortByHeight(self):
        for j in range(0, len(self.boxes)):
            for i in range(0, len(self.boxes)-1):
                if self.boxes[i].height < self.boxes[i+1].height:
                    self.boxes[i+1], self.boxes[i] = self.boxes[i], self.boxes[i+1]
        return True
                
    def createStack(self):
        return 0

# driver code
b1 = box(1,2,3)
b2 = box(4,7,6)
b3 = box(8,9,10)
boxes = StackOfBox([b1, b2, b3])

boxes.printBoxes()
boxes.sortByHeight()
boxes.printBoxes()
print()
print(boxes.maxHeight)

            
    
