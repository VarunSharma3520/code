"""
class Variable and Instance Variable
"""
class human():
    count = 0
    def __init__(self,human,gender): # constructor
        human.count +=1
        self.gender = gender
        self.name = name
    def __del__(self):  # destructor

h1 = human("Varun","M")
h2 = human("Nisha","F")
print(h1.count)
print(h2.count)
print(h1.name)
print(h2.name)
h1.height = 456
