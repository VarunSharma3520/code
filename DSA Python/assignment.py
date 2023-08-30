days = int(input("How many day's temperature ? "))
temp = []
sum = 0
for i in range(days):
    user_temp = int(input("Day(s)",i,"'s high temperature: "))
    temp.append(user_temp)
    sum += user_temp
print("Average: ",sum/days)
