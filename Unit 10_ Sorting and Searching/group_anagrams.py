# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 17:36:24 2019

@author: priya
"""

def grp_anagrams(strings):
    Dict = dict()
    for s in strings:
        key = "".join(ch for ch in sorted(s))
        if key in Dict:
            Dict[key].append(s)
        else:
            Dict[key] = [s]
        
    return [v for value in Dict.values() for v in value]
        
print(grp_anagrams(["thing", "acre", "night", "bb", "abc", "care", "race"]))