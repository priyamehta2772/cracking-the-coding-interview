# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 00:00:28 2019
Power Set
@author: priya
"""

def getSubset(S: list, current: int, result: list):
    if current == len(S):
        print(result, end=" ")
        return
    getSubset(S, current+1, result)
    temp = result.copy()
    temp.append(S[current])
    getSubset(S, current+1, temp)


def getPowerSet(S: list, current: int, result: list) -> list:        
    if current == len(S):
        return result
    x = result[:]
    for i in x:
        result.append(i[:])
    n = len(result)
    for i in range(n//2, n):
        result[i].append(S[current])
    getPowerSet(S, current+1, result)
    return result
       

# Driver code
getSubset([1,2,3], 0, [])
print()
print(getPowerSet([1,2,3], 0, [[]]))








