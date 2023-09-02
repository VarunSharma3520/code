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

# Que2. merge two sorted array
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







