# Parent class
class Animal:
    def eat(self):
        print("Animals can eat")

    def sleep(self):
        print("Animals can sleep")

# Child class
class Dog(Animal):
    def bark(self):
        print("Dog can bark")

# Creating object
d = Dog()

d.eat()
d.sleep()
d.bark()