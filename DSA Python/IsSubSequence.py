'''
    Time complexity: O(N * M)
    Space complexity: O(1)

    where 'N' is number of characters in string 'str1' 
    and 'M' is number of characters in string 'str2'. 
'''

def isSubSequence(str1, str2):

    prev = -1
    count = 0
    n = len(str1)
    m = len(str2)

    # To use iterate all character of 'str2'.
    for i in range(n):  
        for j in range(m):
            if(str1[i] == str2[j] and j > prev):
                prev = j
                count += 1
                break

    # If all characters of 'str1' are present in 'str2' in same order.
    if(count == n):       
        return True
    else:
        return False