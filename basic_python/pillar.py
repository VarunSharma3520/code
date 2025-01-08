"""
There are four basic pillar of OOPs: 
Inheritance
Polymorphisim
Encapsultion
Abstraction

Types of in heritance;
Single Inheritance
Multiple Inheritance
Multilevel Inheritance
Hierarchical Inheritance
Hybrid Inheritance

Q: Does True overloading exist:
A: NO
"""


class Vehicles():
    tyre = True
    def run(self):
        print("I run on petrol")

class Human():
    tyre = False
    def run(self):
        print("I can rum on legs")

class Hetchback(Vehicles,Human): # Example of Multiple Inheritance
    ntyre = 4
    def work(self):
        print("I can go to places")

class Multilevel1(Human):
    level1 = 1

class Multilevel2(Multilevel1):
    level2 = 2

class Single(Human):
    def __init__(self):
        print("this is single")

class Heritance(Vehicles):
    def __init__(self):
        print("Hi")

hi = Heritance()