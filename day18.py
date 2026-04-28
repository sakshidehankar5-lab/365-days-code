#Single Inheritance
class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

d = Dog()
d.eat()   # inherited method
d.bark()  # Dog's own method







#Multiple Inheritance
class Animal:
    def eat(self):
        print("Animal eats food")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Puppy(Dog):
    def weep(self):
        print("Puppy weeps")

p = Puppy()
p.eat()
p.bark()
p.weep()


