import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.
# Lexicographic order creates the next biggest string given an input alphabetical string
#  Given string as "abdc". The next biggest will be "acbd"
# https://www.hackerrank.com/challenges/bigger-is-greater/problem
def biggerIsGreater(w):
    lenw=len(w)
    count=0
    a='no answer'
    if lenw==1:
        return a
    else:
        for i in range(lenw-1,0,-1):
            if w[i]<=w[i-1]:
                count=count+1    
                if count==(lenw-1):
                    return a
                    break
                else:
                    continue
            else:      
                issue_small=w[i-1:]
                str_rem=w[0:i-1]
                alpha=0
                k=1
                len_issue=len(issue_small)
                exc=0
                while (alpha==0):
                        if (issue_small[0]<issue_small[k]) and exc==0:
                            if k<len_issue-1:
                                k=k+1
                            else:
                                exc=1
                        else:
                            if (issue_small[0]>=issue_small[k]):
                                k=k-1
                            issue_small_l=list(issue_small)
                            issue_small_l[0] ,issue_small_l[k]=issue_small_l[k],issue_small_l[0]
                            sort_rem=sorted(issue_small_l[1:])
                            alpha=1
                            str_final=str_rem+issue_small_l[0]+''.join(sort_rem)
                            return str_final
    
strin='abdc'
print (biggerIsGreater(strin)) # print acbd
