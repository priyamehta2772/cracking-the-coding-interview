# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 18:42:03 2019
2.2 Return Kth from last
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
    def get_Kth_from_last(self, k) -> LinkedListNode:
        slow = fast = self.head
        while k:
            if fast is not None:
                fast = fast.link
                k -= 1
            else:
                return None       # returns None if k is greater than length of linked list
        while fast is not None:
            slow = slow.link
            fast = fast.link
        return slow
 
#Driver code
twelve = LinkedListNode(12, None)
ten = LinkedListNode(10, twelve)
nine = LinkedListNode(9, ten)
five = LinkedListNode(5, nine)
one = LinkedListNode(1, five)        

ll = LinkedList(one)
ll.print_list()
res = ll.get_Kth_from_last(6)
if res is None:
    print("Value of K is invalid")
else:
    print(res.value)
    