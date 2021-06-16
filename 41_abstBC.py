#  ......Abstract base class.......

# from abc import ABCMeta,abstractmethod
from abc import ABC,abstractmethod
class shape(ABC) :
    @abstractmethod
    def printarea(self):
        return 0
class Rectangle(shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 5
        self.breadth = 6
    def printarea(self):
        return self.length*self.breadth

area = Rectangle()
# area.printarea()                    # TypeError: Can't instantiate abstract class Rectangle with abstract methods printarea
print(area.printarea())         # 30