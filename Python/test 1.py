# Que1. find fibonaacci terms
user_input = int(input("Enter any number : "))
pre = 0
pro = 1
if user_input == 1:
    print(pre)
if user_input == 2:
    print(pre)
    print(pro)
if user_input > 2:
    print(pre)
    print(pro)
    for i in range(3,user_input+1):
        print(pre+pro)
        c = pre 
        pre = pro
        pro = pro + c

# Que2. merge two sorted array (to be completed)
arr1 = [7,8,10,13,90]
arr2 = [9,11,17,62,81,92]
def merge_two_sorted_array(arr1,arr2):
    checker = 0
    listy = []
    pass
print(merge_two_sorted_array)

# Que3. Remove an element from an array
arr1 = [7,8,10,13,90]
def del_element(arr1,elem):
    listy = []
    for i in range(len(arr1)):
        if arr1[i] != elem:
            listy.append(arr1[i])
    return listy
print(del_element(arr1,13))

# Que4. find third max element
listy = [7,8,110,5,90]
def third_max(arr):
    fmax,smax,tmax = 0,0,0
    for i in range(len(arr)):
        if arr[i] > fmax:
            tmax = smax
            smax = fmax
            fmax = arr[i]
        elif arr[i] > smax:
            tmax = smax
            smax = arr[i]
        elif arr[i] > tmax:
            tmax = arr[i]
        else:
            pass
    return tmax
    
print(third_max(listy))

# Que5. 

# Que6. 

# Que7. Check if an array is ascendin order
listy = [7,8,11,15,90]
def isaccend(arr):
    for i in range(1,len(arr)):
        if arr[i-1]>arr[i]:
            return False
    else:
        return True
print(isaccend(listy))

# Que8. Find the sum of even index in array
listy = [7,8,110,5,90]
def sum_even(arr):
    sum = 0
    for i in range(0,len(arr),2):
        sum += arr[i]
    return sum
print(sum_even(listy))

# Que9. find prime number in a given range

# Que10. Add two numbers represented by array...






