# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 01:21:03 2019

@author: PriyaMehta
"""

def create_memset(words):
    keys = list('abcdefghijklmnopqrstuvwxyz')
    values = [2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]
    letter_to_digit = dict(zip(keys, values))
    def get_num_seq(word):
        return int("".join(str(letter_to_digit[i]) for i in list(word)))
    memset = dict()
    for w in words:
    	seq = get_num_seq(w)
    	if seq in memset:
    		memset[seq].append(w)
    	else:
    		memset[seq] = [w]
    return memset

# driver code
l = ['apple', 'tree', 'used', 'priya']
dictionary = create_memset(l)
print(dictionary)

i = 8733
print(dictionary[i])