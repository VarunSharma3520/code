# programming paradigms (styles of programming)
# 1. structured programming 
# 2. procedural programming 
# 3. object-oriented programming 
# 4. functional programming 



# benifits of oops 
# 1. binding 
# 2. object - an object has 
#           ----> attributes ----> create attributes variables
#           ----> behavior ---> create behavior methods // functions 
# 3. class - is a blueprint/ templates 
# creating a class from syntax -

class Human:
    hair = True
    def walk(self):
        print("Human.walk -> i can walk")
        
class ant: 
    hair = False 
    def run(self):
        print("ant.run -> i can run")
        
h1 = Human()
h2 = Human()
print(h1.hair)
print(h2.hair)
print(h3 = ant)
print(h3.hair)
a1  = ant()
print(a1.hair)
# print(a1.skin)       # creates error as object ant has no skin method or argument 


h1.walk()
class gun:            
    class_1 = 'lmg'
    def fire():
        print("gun.fire -> dun dun dun")
        
g1 = gun()

# the difference between methods and functions is that 
# methods are binded to the class (can be used via object) 
# whereas function can be used indepedently

# ---> all methods are by default functions. 
# ---> all functions are not methods until defined inside a class 
# ---> self is keyword which is used to bind a particular object with its class
# ---> object is an actual implementation of the class
# ---> instance is the virtual copy of the object

class car:
    name = 'ferrari'
    def color(self):
        print("car.color -> red")
c1 = car()
print(c1.color())