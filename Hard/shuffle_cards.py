# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 23:29:00 2019

@author: priya
Shuffle cards
"""
import random

def shuffle1(cards: list) -> list:
    for i in range(len(cards)-1, 0, -1):
        r = random.randint(0,i)
        cards[i], cards[r] = cards[r], cards[i]
    return cards

def shuffle2(cards: list) -> list:
    for i in range(len(cards)):
        r = random.randint(i,len(cards)-1)
        cards[i], cards[r] = cards[r], cards[i]
    return cards

def shuffle3(cards: list, current: int) -> list:
    if current == 0:
        return cards
    shuffle3(cards, current-1)
    r  = random.randint(0,current)
    cards[current], cards[r] = cards[r], cards[current]
    return cards


cards = [i for i in range(1,11)]
for c in shuffle1(cards):
    print(c,end=" ")

print()
for c in shuffle2(cards):
    print(c,end=" ")
    
print()
for c in shuffle3(cards, len(cards)-1):
    print(c,end=" ")
