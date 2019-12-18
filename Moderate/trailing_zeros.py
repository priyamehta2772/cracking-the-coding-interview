# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 01:55:09 2019

@author: priya
"""

def findTrailingZeros(n):             # Geeks for Geeks
    count = 0
    i=5
    while (n/i>=1): 
        count += int(n/i) 
        i *= 5
    return int(count) 

def getTrailingZeros(n: int) -> int:  # Mine
    index_of_5 = 0
    while(n>0):
        index_of_5 += int(n/5)
        n /= 5
    return index_of_5

n=100
print(findTrailingZeros(n))
print(getTrailingZeros(n))
