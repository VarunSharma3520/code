n = 5

# question 1
for i in range(n):
    print("*"*i)

# Question 2
for i in range(n):
    print(" "*(i-1),"*"*(n-i))

# Question 3
for i in range(n+2):
    print()
    for j in range(1,n+2):
        if i > j :
            print(j,end='')

# Question 5 
for i in range(n):
    print(" "*(n-i),"*"*i)

# Question 6

# Question 7

# Question 8

# Question 9
for i in range(1,n+3):
    print()
    for j in range(1,n+3):
        if i > j:
            print(j,end="")

# Question 10
for i in range(1,n+1):
    print(str(i)*i+'\n')



