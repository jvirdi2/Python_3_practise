#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
import numpy as np

def matrix_multiplication(A,B):
    len_A=A.shape
    len_B=B.shape
    if len_A[1]!=len_B[0]:
        print ('Matrix Multiplication is not possible')
        C='Not Defined'
    else:
        C=np.zeros((len_A[0],len_B[1]))
        print ('Matrix multiplication is possible')
        for i in range(len_A[0]):
            for j in range(len_B[1]):
                for k in range(len_A[1]):
                    C[i,j]=C[i,j]+A[i,k]*B[k,j]         
    return C
    
A=np.array([[1,2,4],[3,4,5]])
B=np.array([[5,6],[7,8],[9,10]])

print (matrix_multiplication(A,B))

