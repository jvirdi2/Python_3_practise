# Hard algorithm
# Helps in finding maximum element in an array(list) of size n after queries have been performed
# queries are given as list of lists
# Sample input is like
# 5 3
# Here 5 is size of list, [0 0 0 0 0]. 3 is number of operations. The operations are specified as below
# 1 2 100
# 2 5 100
# 3 4 100
# After the first update list will be 100 100 0 0 0.
# After the second update list will be 100 200 100 100 100
# After the third update list will be 100 200 200 200 100.


def arrayManipulation(n, queries):
    list_entries=[0]*n
    queries_size=len(queries)
    for i in range(queries_size):
        list_entries[queries[i][0]-1]=list_entries[queries[i][0]-1]+queries[i][2]
        if queries[i][1]<=(n-1):
            list_entries[queries[i][1]]=list_entries[queries[i][1]]-queries[i][2]
    maximum_v=x=0
    for i in list_entries:
        x=x+i
        if(maximum_v<x): 
            maximum_v=x
    return maximum_v


if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))
    result = arrayManipulation(n, queries)
    print (result)
