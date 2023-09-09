"""
types of argument:
Required Argument
keyword Arguement
Default Argument
Variable Length Arguement 
"""
# Variable Length Argumet:
"""
Variable Length Argument: Eg-> print()
def add(*a):
    print('a',a)
add(5)
add(5,6,"l",10)
"""

"""
Lamda Function:
"""

z = lambda x: x**2
print(z(2))


sql = lambda k:[i**2 for i in k]
def add():
    l = [1,2,3,4,5,6,7,8,9]
    return sql(l)
print(add())

l = [1,2,3,4,5,6,7,8,9]
print((lambda k : [i**2 for i in k])(l))

swap = lambda x,y: [y,x]
l1 = [1,2,3,4,5]
l2 = [6,7,8,9,0]
l1[0],l1[1] = swap(l1[0],l1[1])
print(l1)

"""
map(funcName,collection)
"""
l = [1,2,3,4,5,6,7,8,9]
n = list(map(str,l))
print(n)

l1 = '123456'
l2 = list(l1)
print([int(x)**2 for x in l2 ])
l3 = list(map(int,l2))
print([x**2 for x in l3 ])
