# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 18:14:27 2019

@author: priya

Q4.9 BST Sequences : Binary search tree was created by traversing through an array from left to 
write and inserting each element. Given a Binary Search Tree, print all possible arrays that 
could have led to this tree.

"""
class BSTNode:
    def __init__(self, v, l, r):
        self.value = v
        self.left = l
        self.right = r
   
class BST:
    def __init__(self, r):
        self.root = r
        self.numOfBSTseq = 0
        self.memset = dict()
        
    def getBSTseq(self, possible: list, result: list) -> None: 
        if len(possible) == 0:
            print(",".join(str(i) for i in result))
            self.numOfBSTseq += 1
            return
        if (len(possible) == 1) and (possible[0] in self.memset):
            for s in self.memset[possible[0]]:
                self.getBSTseq([], result.append(s))            
        for p in possible:
            temp_possible = possible.copy()
            temp_result = result.copy()
            temp_possible.remove(p)
            temp_result.append(p.value)
            if p.left is not None:
                temp_possible.append(p.left)
            if p.right is not None:
                temp_possible.append(p.right)
            self.getBSTseq(temp_possible, temp_result)
            
#    def getBSTseq(self):             ** Method overloading not allowed in python **
#        self.getBSTseq([self.root], [])
#        return True
            
minusone = BSTNode(-1, None, None)
three = BSTNode(3, None, None)
two = BSTNode(2, minusone, three)
six = BSTNode(6, None, None)
eight = BSTNode(8, None, None)
nine = BSTNode(9, eight, None)
seven = BSTNode(7, six, nine)
four = BSTNode(4,two,seven)
    
head = BST(four)
head.getBSTseq([head.root], [])

print(head.numOfBSTseq)
print(head.memset)
