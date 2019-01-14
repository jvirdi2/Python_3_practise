import math
import os
import random
import re
import sys

# Complete the minimum swaps function below.
# function calculates minimum number of swaps to sort sequence if maximum swaps is restricted to 2 
# If the sequence cannot be sorted with the above constraint, chaotic sequence is reported

# The input array q is of consecutive integers only
# Swapping is NOT successive, any 2 elements maybe swapped

def minimumBribes(q):  
    len_A=len(q)
    number_swaps=0
    check_each=[0]*(len_A)
    d=''
    sorted_q=sorted(q)
    for i in range(0,len_A):
        if q==sorted_q:
            break  
        if d=='Too chaotic':
            print (d)
            break
        else:
            for j in range(0,len_A-1-i):
                if q[j]>q[j+1]:
                    temp_1=q[j]
                    temp_2=q[j+1]
                    q[j]=temp_2
                    q[j+1]=temp_1
                    check_each[temp_1-1]=check_each[temp_1-1]+1
                    if check_each[temp_1-1]>2:
                        d= 'Too chaotic'
                        break                 
                    else:
                        number_swaps=number_swaps+1
    if d!='Too chaotic':
        print (number_swaps)


B=[2,3,4,1,5];
# This can be done in 3 swaps with the above constraint
# [2,3,4,1,5]-> [2,3,1,4,5] -> [3,2,1,4,5] -> [1,2,3,4,5]
print (minimumBribes(B))
