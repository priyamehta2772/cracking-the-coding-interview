# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 19:42:27 2019

@author: priya
6.1 Find pill with high weight, use scale only once
"""

def findHeavyPillBottle(bottles: list, weightDiff) -> int:
    # choose last n-1 bottles
    scale = 0
    for i in range(1,len(bottles)):
        scale += i*bottles[i]
    n = len(bottles)-1
    minWeight = int(n*(n+1)/2)
    return round((scale-minWeight)*10)


# driver code    
normalWeight = 1
heavyWeight = 1.1
totalBottles = 20
bottles = [normalWeight for i in range(totalBottles)]
heavyBottle = 5
bottles[heavyBottle] = heavyWeight
print("Weight of pills in", totalBottles,"bottles:")
print(bottles)
print("Index of Heavy pill bottle:", findHeavyPillBottle(bottles, heavyWeight-normalWeight))