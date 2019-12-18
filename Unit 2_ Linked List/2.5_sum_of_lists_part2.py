# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 19:48:52 2019
2.5 sum of lists (Part1: lists are given in forward order)
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
    def append_at_head(self, val) -> LinkedListNode:
        if self.head is None:
            self.head = LinkedListNode(val, None)
        else:
            self.head = LinkedListNode(val, self.head)
        return self.head
    def get_length(self) -> int:
        count = 0
        i = self.head
        while i is not None:
            count += 1
            i = i.link
        return count
    def append_0_at_head(self, difference):
        while difference > 0:
                self.append_at_head(0)
                difference -= 1
    def addition(self, list1, list2):   # add lists directly
        def rec(node1, node2):
            if node1 is None and node2 is None:
                return 0
            add = rec(node1.link, node2.link) + node1.value + node2.value
            self.append_at_head(add % 10)
            return add // 10
        diff = list1.get_length() - list2.get_length()
        if diff > 0:
            list2.append_0_at_head(diff)
        if diff < 0:
            list1.append_0_at_head(-1 * diff)
        carry = rec(list1.head, list2.head)
        if carry:
            self.append_at_head(carry)
        return
    
#Driver code
six = LinkedListNode(6, None)
one = LinkedListNode(1, six)
seven = LinkedListNode(7, one)
l1 = LinkedList(seven)

two = LinkedListNode(2, None)
nine = LinkedListNode(9, two)
five = LinkedListNode(5, nine)
l2 = LinkedList(five)

l1.print_list()
l2.print_list()

l3 = LinkedList(None)
l3.addition(l1, l2)
l3.print_list()

print("---------------------------------------------------")

m = LinkedListNode(9, LinkedListNode(9, LinkedListNode(9, None)))
n = LinkedListNode(9, None)
lm = LinkedList(m)
ln = LinkedList(n)
lm.print_list()
ln.print_list()

l4 = LinkedList(None)
l4.addition(lm, ln)
l4.print_list()

