# -*- coding: utf-8 -*-
"""
Spyder Editor
2.4 Partition the Linked List
This is a temporary script file.
"""

class LinkedListNode:
    def __init__(self, val, link):
        self.value = val
        self.link = link
        
class LinkedList:
    def __init__(self, head):
        self.head = head
        
    def printLL(self):
        temp = self.head
        print("\nLinked List:", end=" ")
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.link
    
    def appendAtHead(self, prev, curr):
        prev.link = curr.link
        curr.link = self.head
        self.head = curr
        return self.head        
        
    def partition(self, pivot):
        prev = self.head
        while( (prev is not None) and (prev.value >= pivot) ):
            prev = prev.link
        if prev is None:
            return self.head
        curr = prev.link
        while curr is not None:
            if curr.value < pivot:
                temp = curr.link
                self.appendAtHead(prev, curr)
                curr = temp
            else:
                prev = curr
                curr = curr.link

# Driver Code
h = LinkedListNode(3, LinkedListNode(8, LinkedListNode(3, LinkedListNode(5, LinkedListNode(5, LinkedListNode(10, LinkedListNode(2, LinkedListNode(1, None))))))))
ll = LinkedList(h)
ll.printLL()
ll.partition(5)
ll.printLL()