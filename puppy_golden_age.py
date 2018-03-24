#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 13:53:46 2018

@author: bijayamanandhar
"""
def puppy_golden_age(array):
     
    sum, sum_max = 0, 0
    for i in range(len(array)):
        for j in range(i, len(array)):
            
            sum += array[j]
            if sum > sum_max:
                sum_max = sum
                x, y = i, j
        sum = 0
                
    return [x, y]

print(puppy_golden_age([100, -101, 200, -3, 1000]) == [2, 4])
print(puppy_golden_age([5, 3, -5, 1, 19, 2, -4]) == [0, 5])
