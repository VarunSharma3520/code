"""
class Variable and Instance Variable
"""

class Human():
    count = 0
    def __init__(self,name,gender): # constructor
        Human.count +=1
        self.gender = gender
        self.name = name
    def __del__(self):  # destructor
        Human.count -=  1

h1 = Human("Varun","M")
h2 = Human("Nisha","F")
print(h1.count)
print(h2.count)
print(h1.name)
print(h2.name)
h1.height = 456
