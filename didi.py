# The code below takes as input a number N. The task is that
# number 5 can be added  at any spot of this number only once
# and you have to output the largest number
# N=300 Output= 5300
# N=600 Output =6500
# N=-300 Output= -3005
# N=10 Output=510
# N=-10 Output=-105

def solution(N):
    # write your code in Python 3.6
   
    counter=0
    ans_N=[]
    
    if N>=0:
        string_N=str(N)
        for i in string_N:
            if int(i)<=5 and counter==0:
                ans_N.append(5)
                ans_N.append(int(i))
                counter=1
            else:
                ans_N.append(int(i))
        if counter==0:
            ans_N.append(5)
        final_ans=int(''.join(map(str, ans_N)))
    else:
        N_new=(-1)*N
        string_N_new=str(N_new)
        for i in string_N_new:
            if int(i)>5 and counter==0:
                ans_N.append(5)
                ans_N.append(int(i))
                counter=1
            else:
                ans_N.append(int(i))
        if counter==0:
            ans_N.append(5)
        final_ans=int(''.join(map(str, ans_N)))
        final_ans=(-1)*final_ans
    
    
    return final_ans
   
