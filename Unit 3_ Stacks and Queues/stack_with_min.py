# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 23:08:17 2019
Find min element in stack in O(1)
@author: priya
"""

import math

class Stack:
    def __init__(self):
        self.values = []
        self.minTillNow = []
        self.top = -1
    
    def push(self, n) -> bool:
        self.values.append(n)
        if self.top == -1 or self.minTillNow[self.top] > n:
            self.minTillNow.append(n)
        else:
            self.minTillNow.append(self.minTillNow[self.top])
        self.top += 1
        return True

    def pop(self):
        if self.top != -1:
            n = self.values.pop()
            self.minTillNow.pop()
            self.top -= 1
            return n
        return math.inf
    
    def getMin(self):
        if self.top != -1:
            return self.minTillNow[self.top]
        else:
            return math.inf
        
        
# Driver Code
myStack = Stack()
print(myStack.getMin())
myStack.push(8)
print(myStack.getMin())
myStack.push(1)
print(myStack.getMin())
myStack.push(0)
print(myStack.getMin())
myStack.push(2)
print(myStack.getMin())
myStack.push(5)
print(myStack.getMin())
myStack.push(3)
print(myStack.getMin())

print("Val:", myStack.values)
print("Min:",myStack.minTillNow)

myStack.pop()
myStack.pop()
myStack.pop()
myStack.pop()

print(myStack.getMin())
print("Val:", myStack.values)
print("Min:",myStack.minTillNow)
