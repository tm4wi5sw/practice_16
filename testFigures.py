#python 3.8.1
from figures import Rectangle, Square, Circle

r1 = Rectangle(10, 5)

print ("r1.width = ", r1.width)
print ("r1.height = ", r1.height)
print ("r1.getWidth = ", r1.getWidth())
print ("r1.getHeight = ", r1.getHeight())

print ("r1.getArea() = ", r1.getArea())

#---------------------------------------

r2 = Rectangle(3, 4)
r3 = Rectangle(12, 5)

s1 = Square(5)
s2 = Square(10)

c1 = Circle(7)
c2 = Circle(12)

#---------------------------------------

figures = [r1, r2, r3, s1, s2, c1, c2]

for figure in figures:
    if isinstance(figure, Square):
        print(figure.getFigureToStr() + "    S = ", figure.getAreaSquare())
    else:
        print(figure.getFigureToStr() + "    S = ", figure.getArea())