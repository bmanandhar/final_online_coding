#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 14:07:14 2018

@author: bijayamanandhar
"""

def combine_arrays(array1, array2):
    
    array = array1 + array2
    
    # bubble-sort follows
    
    for i in range(len(array) -1):
        for j in range(len(array) -1 -i):
            if array[j] > array[j +1]:
                array[j], array[j +1] = array[j +1], array[j]

    return array

print(combine_arrays([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6])
print(combine_arrays([9, 3, 0], [7, 3, 8]) == [0, 3, 3, 7, 8, 9])

