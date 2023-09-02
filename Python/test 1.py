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
    pass
print(merge_two_sorted_array)

