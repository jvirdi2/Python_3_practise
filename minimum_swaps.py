import math
import os
import random
import re
import sys

# Complete the minimum swaps function below.
# The input array q is of consecutive integers only
# Swapping is NOT successive, any 2 elements maybe swapped. Find minimum swaps to sort sequence

def minimumSwaps(arr):
    arr_sorted=sorted(arr)
    len_arr=len(arr)
    min_swaps=0
    hash_table={}
    for i,v in enumerate(arr):
            hash_table[v]=i
    for i in range(len_arr):
        if arr==arr_sorted:
            break          
        if arr[i]!=arr_sorted[i]:
            start_from_low_end=arr_sorted[i]
            temp=arr[i]
            index=hash_table[start_from_low_end]
            arr[i]=start_from_low_end
            arr[index]=temp
            hash_table[arr_sorted[i]]=i
            hash_table[temp]=index
            min_swaps=min_swaps+1
    return min_swaps

B=[2,3,4,1,5];
# This can be done in a minimum of 3 swaps with the above constraint
# [2,3,4,1,5]-> [2,3,1,4,5] (swap 1)-> [2,1,3,4,5] (swap 2) -> [1,2,3,4,5] (swap 3)
print (minimumSwaps(B))
