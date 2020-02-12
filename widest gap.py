# n denotes number of car slots numbered from 1 to n
# start is an array of starting car positions
# end is an array comprising corresponding end car positions
# goal is to find widest gap where no car is present
# Say car has starting postion of 3 and ending position of 5
# It occupies slots 3,4 and 5. However, another car could also be
# parked parallel to it, whose starting position maybe 4 and ending
# position 7. The car can also have say starting and ending position
# as same value

# Algorithm works as follows. The places that cars occupy are removed
# from list 1,2....n. Try and except is used so that remove command does
# not have an error (eg if an array is [2,4,10], one cannot remove 8. Except
# catches that. 

def widest_gap(n,start,finish):
    lane_list=list(range(1,n+1))
    number_of_cars=len(start)

    for i in range(0,number_of_cars):
        try:
            for j in range(start[i],finish[i]+1):
                lane_list.remove(j)
        except:
            continue
    print(lane_list)
    
# Below code, Helps in finding sub arrays within the main array, having successive elments. 
    len_lane_list=len(lane_list)
    if len_lane_list==0:
            return 0
    else:
        lane_list.append(-1) # added -1 as the end element so that computation is done correctly. Otherwise, last element has an issue
        gap=1
        list_of_gaps=[]
        for i in range(0,len_lane_list):
                if lane_list[i+1]==(1+lane_list[i]):
                    gap=gap+1
                else:
                    list_of_gaps.append(gap)
                    gap=1
        print(list_of_gaps)              
        return max(list_of_gaps)

        
n=10
#start=[8,2,5,1]
#finish=[10,2,6,2]
#start=[3,8,5]
#finish=[3,10,7]
start=[1,7]
finish=[5,10]
print(widest_gap(n,start,finish))
