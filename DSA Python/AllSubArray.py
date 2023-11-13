def subArrayCount(arr, k):
    l = len(arr)
    count = 0 
    for i in range(0,l):
        for j in range(i,l):
            if sum(arr[i:j+1])%k == 0:
                count += 1
    return count
            
            
            
            
            
arr = [5,0,2,3,1]
k = 5
print(subArrayCount(arr,k))
