# Exception Handling
# Exception is which can interrupt program functioning while excecuting script


'''
try:
except:
else:
finally:
'''


'''
In case of error:
try:
except:
finally:
In case of error not occured:
try:
else:
finally:
'''


# Method 1 

# def script():
#     marks = int(input("Enter any number..."))
#     if marks > 40 :
#         print("pass")
#     else:
#         print("fail")
# try:
#     script()
# except:
#     print("An Error Occured ")
#     script()

# Method 2

# def script():
#     marks = int(input("Enter any number..."))
#     return marks
# try:
#     marks = script()
# except:
#     print("An Error Occured ")
#     marks = script()
# else:
#     if marks > 40 :
#         print("pass")
#     else:
#         print("fail")

# Method 3

# try:
#     marks = int(input("Enter any number..."))
# except:
#     print("An Error Occured ")
# else:
#     if marks > 40 :
#         print("pass")
#     else:
#         print("fail")

# try:
#     m = int(input())
#     if m == 1: print(len(m))
#     elif m == 2: import yoyo
#     else: print({1:3}[5])
# except TypeError:
#     print("TypeError")
# except ValueError:
#     print("TypeError")
# except:
#     print("Some Error")
# else:
#     print("Worked Perfectly")