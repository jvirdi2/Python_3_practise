#This is a demo task.
#Write a function:
#that, given an array A of N integers, returns the smallest positive integer (greater than 0)
#that does not occur in A.
#For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
#Given A = [1, 2, 3], the function should return 4.
#Given A = [−1, −3], the function should return 1.
#Given A=[2], function should return 1
#Write an efficient algorithm for the following assumptions:
#N is an integer within the range [1..100,000];
#each element of array A is an integer within the range [−1,000,000..1,000,000].
#Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.


def solution(A):
    # write your code in Python 3.6
    sorted_A=sorted(A)
    len_A=len(sorted_A)
    index=0
    final_ans=0
    counter=0
    if sorted_A[-1]<=0: # Case 1: Handles cases where no positive numbers
        return 1
    
    for i in range(len_A):
        if sorted_A[i]<=0:
            sorted_A[i]=1

        else:
            index=i
            break

    if sorted_A[index]>=2: # Case 2: Handles almost every case where the first positive number in the list that we come across is greater than 2
        return 1
    
    
    else: # Case 3: Handles cases where some negative and positive numbers/all positive numbers
        for i in range(index,len_A):
       
            if i==len_A-1:
                final_ans=sorted_A[i]+1
                return final_ans
            
            if counter==1:
                break
            else:
                possible_value=sorted_A[i]+1
                for j in range(i+1,len_A):
                    if sorted_A[j]==possible_value:
                        break
                    if j==len_A-1 and sorted_A[j]!=possible_value:
                        final_ans=possible_value
                        counter=1
                        return final_ans
                
        

            
            
            

    

    

