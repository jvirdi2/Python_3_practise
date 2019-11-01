from itertools import combinations
def count_duplicates(A):
    B={}
    for i in A:
        try:
            if B[i]>0:
                B[i]=B[i]+1
        except:
            B[i]=1
    return B

# Below code is not very optimised but it is able to do:    
# Case 1
# list_string=['ab','bc','cd','ef']
# Output=6 ('abcdef')

# list_string=['gen','aet']
# Output=0

# list_string=['gen','aet','g123']
# Output=7 ('aetg123')

# The code below finds a concatenated combination such that all 
# of its characters are unique and it is the longest possible such
# combination (the above example demonstrates this)

def solution(list_string):
    len_list_string=len(list_string)
    size=[]
    
    
    for i in range(1,len_list_string):
        current=list(combinations(list_string,i+1))
        for j in current:
            current_element=j
            combined_string=''.join(current_element)

            B={}
            count=0
            for m in combined_string:

                try:
                    if B[m]>0:
                        B[m]=B[m]+1
                        if B[m]>=2:
                            count=1
                            size.append(0)
                            break
                except:
                    B[m]=1
            if count==0:
                size.append(len(combined_string))
            
    return max(size)
                    
    
