
# 1. Encapsulation
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

s1 = Student("Rahul", 85)
s1.display()










# 2. Inheritance
class Animal:
    def speak(self):
        print("Animal makes sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()
d.bark()













# 3. Polymorphism
class Bird:
    def sound(self):
        print("Bird chirps")

class Cat:
    def sound(self):
        print("Cat meows")

b = Bird()
c = Cat()

b.sound()
c.sound()







# 4. Abstraction
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        print("Area:", self.side * self.side)

s = Square(4)
s.area()
