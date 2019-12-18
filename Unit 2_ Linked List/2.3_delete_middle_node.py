# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 18:28:45 2019
2.3 Delete any middle node
@author: PriyaMehta
"""

class LinkedListNode:
    def __init__(self, val, link):
        self.value = val
        self.link = link
        
class LinkedList:
    def __init__(self, h):
        self.head = h
    def print_list(self):
        print("\nList: ", end="")
        i = self.head
        while i is not None:
            print(i.value, end=" ")
            i = i.link
    def delete_middle_node(self, node: LinkedListNode):  #cannot handle case where node is last node of linked list
        while True:
            node.value = node.link.value
            if node.link.link is None:
                node.link = None
                break
            node = node.link
        return True
    
    
# Driver code

twelve = LinkedListNode(12, None)
ten = LinkedListNode(10, twelve)
nine = LinkedListNode(9, ten)
five = LinkedListNode(5, nine)
one = LinkedListNode(1, five)        

ll = LinkedList(one)
ll.print_list()
ll.delete_middle_node(five)
ll.print_list()
