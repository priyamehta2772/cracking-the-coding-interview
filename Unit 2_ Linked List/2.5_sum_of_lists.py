# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 19:09:00 2019
2.5 sum of lists (Part1: lists are given in reverse order)
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
        print()
    def append_at_tail(self, val) -> LinkedListNode:
        if self.head is None:
            self.head = LinkedListNode(val, None)
        else:
            i = self.head
            while i.link is not None:
                i = i.link
            i.link = LinkedListNode(val, None)
        return self.head
    def addition(self, list1, list2):   # directly adding lists
        def rec(node1, node2, carry):
            if node1 is None and node2 is None:
                if carry:
                    self.append_at_tail(carry)
                return
            add = carry
            next1 = None
            next2 = None
            if node1 is not None:
                add += node1.value
                next1 = node1.link
            if node2 is not None:
                add += node2.value
                next2 = node2.link
            val = add % 10
            self.append_at_tail(val)
            rec(next1, next2, add//10)
            return
        rec(list1.head, list2.head, 0)
    
#Driver code
six = LinkedListNode(9, None)
one = LinkedListNode(8, six)
seven = LinkedListNode(7, one)
l1 = LinkedList(seven)

two = LinkedListNode(7, None)
nine = LinkedListNode(8, two)
five = LinkedListNode(9, nine)
l2 = LinkedList(five)

l1.print_list()
l2.print_list()

#l3 = LinkedList(None)
#l3.summation(l1, l2)
#l3.print_list()

l3 = LinkedList(None)
l3.addition(l1, l2)
l3.print_list()
