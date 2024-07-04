# Q1: Find number of days above average temperature...
days = int(input("How many day's temperature ? "))
temp = []
sum = 0
for i in range(days):
    user_temp = int(input("Day(s) "+str(i+1)+"'s high temperature: "))
    temp.append(user_temp)
    sum += user_temp
avg = sum/days
sum = 0
print("Average = ",avg)
for i in range(len(temp)):
    if temp[i] > avg:
        sum = sum + 1
print(sum,"day(s) above average")

# Q2: Find the pair of all numbers whose sum is given number:
user_input = int(input("Enter any number : "))
for i in range(user_input//2+1):
    print("{",i,",",user_input-i,"}")
