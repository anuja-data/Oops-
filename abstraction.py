from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def area(self):
        print("Area of Rectangle:", 20 * 10)

obj = Rectangle()
obj.area()