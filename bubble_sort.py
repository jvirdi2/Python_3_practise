

def bubble(A):
    len_A=len(A)
    for i in range(0,len_A):
        for j in range(0,len_A-1-i):
            if A[j]>A[j+1]:
                temp_1=A[j]
                temp_2=A[j+1]
                A[j]=temp_2
                A[j+1]=temp_1
    return A

A=[2,1,3,2,0,-1]
print (bubble(A))
            
    
