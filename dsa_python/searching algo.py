# Types of searching algo
# 1. Linear search for sorted and unsorted array
# 1. Binary search for sorted only

def Linear(arr,elem):
    # it has complexity O(n)
    for i in range(len(arr)):
        if elem == arr[i]:
            return [elem,i]
    
def Binary(arr,elem):
    # it has complexity O(log(n))
    start = 0
    end = len(arr) - 1
    while start <= end:
        
        mid = start + (end - start)//2
        # mid = (end + start)//2 not work in c++ 2*31 - 1 so it will create error

        
        if arr[mid] == elem:
            return [elem,mid]
            
        #below two if makes code even faster
        if arr[start] == elem:
            return [elem,start]
        if arr[end] == elem:
            return [elem,end]
            
        # positioning
        if arr[mid] < elem:
            start = mid + 1
        else:
            end = mid - 1
    
    else:
        return None
                
def BinaryFast(arr,elem):
    # it has complexity O(log(n))
    start = 0
    end = len(arr) - 1
    while start <= end:
        
        mid = start + (end - start)//2
        
        if arr[mid] == elem:
            return [elem,mid]
            
        #below two if makes code even faster
        if arr[start] == elem:
            return [elem,start]
        if arr[end] == elem:
            return [elem,end]
            
        # positioning
        if arr[mid] < elem:
            start = mid + 1
        else:
            end = mid - 1
    
    else:
        return None
arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
# print(Linear(arr,15))
# print(Binary(arr,20))
# print(BinaryFast(arr,21))