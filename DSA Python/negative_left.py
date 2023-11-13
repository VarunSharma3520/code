# Move All Negative Numbers To Beginning And Positive To End
#TODO https://www.codingninjas.com/studio/problems/move-all-negative-numbers-to-beginning-and-positive-to-end_1112620?utm_source=youtube&utm_medium=affiliate&utm_campaign=parikh_youtube


def separateNegativeAndPositive(nums):
    modified = False
    found = False
    for i in range(len(nums)):
        if nums[i] > 0:
            found = True
        if nums[i] < 0 and found:
            modified = True
    if modified:
        return 'Yes'
    else:
        return 'No'
    
    
nums = [1,2]
print(separateNegativeAndPositive(nums))