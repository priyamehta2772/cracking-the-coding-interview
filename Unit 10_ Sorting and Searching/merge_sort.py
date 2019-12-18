# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 16:49:49 2019
merge sort
@author: PriyaMehta
"""

def merge_sort(array):
    if len(array) == 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(array, left, right)
    
def merge(N, A, B):
    i = j = k = 0
    while i < len(A) and j < len(B):
        if A[i] > B[j]:
            N[k] = B[j]
            j += 1
        else:
            N[k] = A[i]
            i += 1
        k += 1
    while i < len(A):
        N[k] = A[i]
        k += 1
        i += 1
    while j < len(B):
        N[k] = B[j]
        k += 1
        j += 1
    return N
    
# driver code
x = [5,9,1,6,2,7,0,7,4]
print(x)
merge_sort(x)
print(x)
    
