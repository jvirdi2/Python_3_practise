import math
def merge(A,B):
# Merges 2 sorted lists to make a sorted resultant list
    len_A=len(A)
    len_B=len(B)
    len_C=len_A+len_B
    C=[math.inf]*(len_C)
    ind,i,j=0,0,0
    while (ind<len_C):
        if ((i<len_A) & (j<len_B)):
            if ((A[i]<B[j])):
                C[ind]=A[i]
                ind=ind+1
                i=i+1
                if i==(len_A):              
                    break
            if ((A[i]>=B[j])):
                C[ind]=B[j]
                ind=ind+1
                j=j+1
        else:
            break

    if ((C[ind-1]==A[-1]) & (C[ind-1]!=B[-1])):
        C[ind:]=B[j:]
    else:
        C[ind:]=A[i:]
                     
    return C

            
def merge_sort(A):
    len_A=len(A)
    if len_A==1:
        return A
    else:
        seq1=A[0:int(len_A/2)]
        seq2=A[int(len_A/2):]
        return merge(merge_sort(seq1),merge_sort(seq2))

A=[1,2,3,1,1,0,5,2]
print (merge_sort(A))

    
