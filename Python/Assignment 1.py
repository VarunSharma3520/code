# 1. WAP to take 10 numbers from a user and calculate their mean...
sum = 0
for i in range(10):
    user_input = int(input("Enter any number..."))
    sum = sum + user_input
print("mean of above number is : ",sum/10)


# 2. Display numbers divisible by 5 from a list.
listy = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in listy:
    if i % 5 == 0:
        print(i)


#3. WAP to calculate the number of elements in a string, taken as input from the user, without using len function.
user_input = input("Enter any string...")
count = 0
for i in user_input:
    count +=1
print("Length of string is : ",count)


#4. WAP to check if a number is even or odd where number is taken as input.
user_input = int(input("Enter any number..."))
if user_input % 2 == 0:
    print(user_input,"is a even number")
else:
    print(user_input,"is a odd number")


#5. Write a Python program to find the sum of the first n positive integers. Take n as input from the user.
n = int(input("Enter any number..."))
print((n*(n+1))/2)


#6. WAP to print all the strings present in a list in reverse fashion.
listy = ["varun","sharma","54846511654","@#$%^&*()","ok"]
for i in range(len(listy)):
    print(listy[i][::-1])


#7. Print characters from a string that are present at an even index number.
string = "varun_sharma_0268"
for i in range(0,len(string),2):
    print(string[i])


#8. Check if the first and last number of a list is the same
listy = [0,3,5,6,4,0,4,6,4,4,3,3]
if listy[0] == listy[-1]:
    print("first and last number of a list are the same")
else:
    print("first and last number of a list arn't the same")


#9. Calculate income tax for the input income by adhering to the Indian rules.
user_income = int(input("Enter your income..."))
if user_income < 250000:
    print("Hey! you are tax free...")
elif user_income > 250000 and user_income <= 500000:
    print("5 percent above ₹ 2,50,000")
elif user_income > 500000 and user_income <= 750000:
    print("₹ 12,500 + 10 percent above ₹ 5,00,000")
elif user_income <750000 and user_income <= 1000000:
    print("₹ 37,500 + 15 percent above ₹ 7,50,000")
elif user_income > 1000000 and user_income <= 1250000:
    print("₹ 75,000 + 20 percent above ₹ 10,00,000")
elif user_income > 1250000 and user_income <= 1500000:
    print("₹ 1,25,000 + 25 percent above ₹ 12,50,000")
else:
    print("₹ 1,87,500 + 30 precent above ₹ 15,00,000")


#10. Write a Python program to check whether a string starts with vowel or not.
string = "varun sharma"
if string[0] in "aeiouAEIOU":
    print("string starts with vowel")
else:
    print("string do not starts with vowel")


#11. Write a Python program to check if all the characters of a string are vowel or not.
string = "Varun Sharma"
result = 0
for i in string:
    if i not in "aeiouAEIOU":
        result = 1
if result == 0:
    print("string has all vowels")
else:
    print("string do not contain all vowels")


#12. WAP to calculate percentage of a student through 5 subjects. Take marks as input from the user.
student_name = input("enter student name...")
maths = int(input("Enter your maths marks..."))
phy = int(input("Enter your physics marks..."))
chem = int(input("Enter your chemistry marks..."))
comp = int(input("Enter your computer marks..."))
eng = int(input("Enter your english marks..."))
print(student_name,"has successfully passed with : ",(maths + phy + chem + comp + eng)/5)


#13. WAP to convert '95.3' taken as input from the user into float value.
user_input = float(input("Enter any nuumber"))
print(type(user_input))


#14. Write a Python program to count the number of even and odd numbers from a list of numbers. e.g. i\p: [1, 2, 3, 4, 5, 6, 7, 8, 9]
listy = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd = 0
even = 0
for i in range(len(listy)):
    if listy[i] % 2 == 0:
        even += 1
    else:
        odd += 1
print("Total no of even number : ",even)
print("Total no of odd number : ",odd)


#@15. WAP to calculate the surface area of a triangle. Take the required values as input.
base = int(input("Enter the value of base of a triangle : "))
height = int(input("Enter the value of height of a triangle : "))
print("area of triangle : ",0.5*base*height)







