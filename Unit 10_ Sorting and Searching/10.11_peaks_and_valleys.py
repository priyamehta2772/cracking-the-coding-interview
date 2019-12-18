# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 16:46:23 2019
10.11 Peaks and Valleys
@author: PriyaMehta
"""

def sort_by_valleys(array):   # Time complexity: O(n*log(n))
	array = sorted(array)
	for i in range(2, len(array), 2):
		if array[i] > array[i-1]:
			array[i], array[i-1] = array[i-1], array[i]
	return array
    

def sort_peaks_valleys(array):   # Time complexity: O(n)
    if len(array) < 3:
        return array
    if array[0] > array[1]:
        array[0], array[1] = array[1], array[0]
    for i in range(2, len(array), 2):
        if array[i] > array[i-1]:
            array[i], array[i-1] = array[i-1], array[i]
        if i+1 < len(array) and array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
    return array

# Driver code
A = [int(i) for i in input().split()]
print(sort_by_valleys(A))
print(sort_peaks_valleys(A))