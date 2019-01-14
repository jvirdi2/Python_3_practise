import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
# the ith element of array can bribe the (i-1) element in front to swap position
# this swapping can be done max of 2 times
# Find minimum number of bribes to make a standard sequence come into current chaotic state
# The array has consecutive integers as elements starting from 1
# function calculates minimum number of swaps to sort sequence if maximum swaps is restricted to 2 (forward directional swaps-bigger number comes to the left )
# If the sequence cannot be sorrted with the above constrainet, chaotic sequence is reported
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
    
A=[2,5,1,3,4] # Too chaotic
print (minimumBribes(A))
B=[2,1,5,3,4] # 3 bribes done
print (minimumBribes(B))
