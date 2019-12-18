# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 14:14:19 2019
Quick sort
@author: PriyaMehta
"""
def partition(array, start, end) -> int:
        pivot = array[end]
        p_index = start
        for i in range(start, end):
            if array[i] <= pivot:
                array[i], array[p_index] = array[p_index], array[i]
                p_index += 1
        array[p_index], array[end] = array[end], array[p_index]
        return p_index
    
def quick_sort(array: list, start: int, end: int):   
    if start >= end:
        return
    p_index = partition(array, start, end)
    quick_sort(array, start, p_index-1)
    quick_sort(array, p_index+1, end)

# driver code
    
l = [5,9,1,6,2,7,0,7,4]
#l = [7, 2, 1,6, 8, 5, 3, 4]
print(l)
quick_sort(l, 0, len(l)-1)
print(l)