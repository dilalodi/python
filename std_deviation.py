# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 18:12:59 2022
Standard Deviation Algorithm -- by DLLD 04/01/22
@author: dllopezd
"""
## 0. FIRST_LIST & SECOND_LIST: Create number list
first_list = [1,2,3]
second_list=[]

## 1. NUMBER: Counts the number of elements in an first_list, stores it in v_N
v_N=len(first_list)
## 2. AVG: Add the elements of the first_list and divide them by N, stores it in v_avg
v_avg= sum(first_list)/v_N

## 3. LOOP: For each element in first_list, less v_avg & squares it, stores it in 2nd_list
for n in first_list:
    v_loop = (n - v_avg)**2
    second_list.append(v_loop)

## 4. TOTAL: Add the elements of the 2nd_list and divide them by N
v_total= sum(second_list)/v_N
print(v_total)
