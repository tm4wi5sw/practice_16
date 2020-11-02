#python 3.8.1
class Rectangle:
    def __init__ (self, width, height):
        self.width = width
        self.height = height
    
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height

    # метод расчёта площади
    def getArea(self):
        return self.width * self.height

    # вернуть фигуру строкой    
    def getFigureToStr(self):
        return "Rectangle(" + str(self.width) +", "+ str(self.height) + ")"

class Square:
    def __init__ (self, width):
        self.width = width
        self.height = width

    # метод расчёта площади
    def getAreaSquare(self):
        return self.width ** 2

    # вернуть фигуру строкой    
    def getFigureToStr(self):
        return "Rectangle(" + str(self.width) +", "+ str(self.height) + ")"

class Circle:
    def __init__(self, radius):
        self.radius = radius

    # метод расчёта площади
    def getArea(self):
        return 3.14 * self.radius ** 2

    # вернуть фигуру строкой    
    def getFigureToStr(self):
        return "Circle(" + str(self.radius) + ")"
