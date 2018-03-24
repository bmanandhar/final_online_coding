#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 14:09:36 2018

@author: bijayamanandhar
"""

def subsets(s):
    
    if s == []: return [s]
    
    sets = [s]
    for i in range(len(s)):
        temp_subsets = subsets(s[:i] + s[i+1:])
        for subset in temp_subsets:
            if subset not in sets:
                sets.append(subset)
    return sets

print(subsets(['a', 'b', 'c']))
print(subsets([1, 2, 3]))