# Merge sort practise

# returns merged sorted list from 2 two smaller sorted lists

class sorting():
    
    def merge_sort(self,list_entry):
        len_list=len(list_entry)
        mid=int(len_list/2)
        if len_list==0 or len_list==1:
            return list_entry
        else:
            return self.merge(self.merge_sort(list_entry[0:mid]),self.merge_sort(list_entry[mid:]))
        
    def merge(self,A,B):
        len_A=len(A)
        len_B=len(B)
        combined=[0]*(len_A+len_B)
        i=0
        j=0
        
        if len_A==0:
            return B
        elif len_B==0:
            return A
        else:
            while i<=len_A:
                while j<=len_B:
                    
                    
                    if i<len_A and j<len_B:

                        if A[i]<B[j]:
                            combined[i+j]=A[i]
                            i=i+1
                        elif A[i]>B[j]:
                            combined[i+j]=B[j]
                            j=j+1
                            
                        else:
                            combined[i+j]=A[i]
                            combined[i+j+1]=B[j]
                            i=i+1
                            j=j+1
                            
                    else:
                        if j>=(len_B):
                            combined[i+j:]=A[i:]
                            i=len_A+1
                            break
                        if i>=(len_A):
                            combined[i+j:]=B[j:]
                            i=len_A+1
                            break
                        
            return combined

    def bubble_sort(self,list_entry):
        len_list=len(list_entry)
        for m in range(1,len_list):
            for i in range(len_list-m):
                if list_entry[i]>list_entry[i+1]:
                    temp=list_entry[i]
                    list_entry[i]=list_entry[i+1]
                    list_entry[i+1]=temp

        return list_entry

    def quick_sort(self,list_entry):
        len_list=len(list_entry)
        
        before_pivot=[]
        after_pivot=[]
        
        if len_list==1 or len_list==0:
            return list_entry
        else:
            pivot=list_entry[0]
            for i in range(1,len_list):
                if list_entry[i]<=pivot:
                    before_pivot.append(list_entry[i])
                else:
                    after_pivot.append(list_entry[i])

            final=self.quick_sort(before_pivot)+[pivot]+self.quick_sort(after_pivot)

        return final
        
            
            

    
    

A=sorting()
list_entry=[3,1,5,7,2]
print(A.bubble_sort(list_entry))
            
