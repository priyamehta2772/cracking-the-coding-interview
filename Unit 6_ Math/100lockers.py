# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 16:35:09 2019

@author: priya
100 lockers
"""

def toggle(lockers: list) -> int:
    for i in range(1, len(lockers)+1):
        start = i-1
        while start<=99:
            lockers[start] = not lockers[start]
            start += i
    return lockers.count(True)

l = [False]*100
print(toggle(l))