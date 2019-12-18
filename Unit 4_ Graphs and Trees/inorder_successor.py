# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 17:18:24 2019

@author: priya
Find next in-order successor for a given node
"""
class TreeNode:
    def __init__(self, val, left, right, parent):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def setParent(self, p):
        self.parent = p

class Tree:
    def __init__(self, root: TreeNode):
        self.root = root

    def getSuccessor(self, n: TreeNode):
        result = None
        if n.left is None and n.right is None and n.parent is None:
            return None
        if n.right is not None:
            result = n.right
            while result.left is not None:
                result = result.left
            return result
        else:
            result = n.parent
            if result.val > n.val:
                return result
            while result.val<n.val:
                if result.parent is None:
                    return None
                result = result.parent
            return result
  
# Driver code      
seven = TreeNode(7, None, None, None)
five = TreeNode(5, None, seven, None)
nine = TreeNode(9, None, None, None)
eight = TreeNode(8, five, nine, None)
eleven = TreeNode(11, None, None, None)
twelve = TreeNode(12, eleven, None, None)
fourteen = TreeNode(14, None, None, None)
thirteen = TreeNode(13, twelve, fourteen, None)
eighteen = TreeNode(18, None, None, None)
fifteen = TreeNode(15, thirteen, eighteen, None)
ten = TreeNode(10, eight, fifteen, None)

seven.setParent(five)
five.setParent(eight)
nine.setParent(eight)
eight.setParent(ten)
eleven.setParent(twelve)
twelve.setParent(thirteen)
thirteen.setParent(fifteen)
fourteen.setParent(thirteen)
eighteen.setParent(fifteen)
fifteen.setParent(ten)

root = Tree(ten)

node = ten
ans = root.getSuccessor(node)
print("No successor") if ans is None else print(ans.val)
