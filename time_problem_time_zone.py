import math
import os
import random
import re
import sys
from datetime import datetime
from dateutil import parser
# Helps in calculating the difference between time hours in 2 seperate zones

# Complete the time_delta function below.
def time_delta(t1, t2):
    a1=parser.parse(t1)
    a2=parser.parse(t2)
    diff=a1-a2
    time_abs=abs(diff.total_seconds())
    return time_abs

t1='Sat 02 May 2015 19:54:36 +0530'
t2='Fri 01 May 2015 13:54:36 -0000'
print (time_delta(t1,t2))
