from datetime import datetime
import math

class GeometricObject:
    def __init__(self, color='white', filled=False):
        self.__color = color
        self.__filled = filled
        self.__dateCreated = datetime.now()

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def isFilled(self):
        return self.__filled

    def setFilled(self, filled):
        self.__filled = filled

    def getDateCreated(self):
        return self.__dateCreated

    def setDateCreated(self, dateCreated):
        self.__dateCreated = dateCreated

    def __str__(self):
        return f"Created on {self.__dateCreated.strftime('%Y-%m-%d %H:%M:%S')}\nColor: {self.__color}\nFilled: {self.__filled}"

class Circle(GeometricObject):
    def __init__(self, radius=1.0, color='white', filled=False):
        super().__init__(color, filled)
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        self.__radius = radius

    def getArea(self):
        return math.pi * self.__radius ** 2

    def getPerimeter(self):
        return 2 * math.pi * self.__radius

    def __str__(self):
        area = self.getArea()
        perimeter = self.getPerimeter()
        dateCreated = self.getDateCreated().strftime("%Y-%m-%d %H:%M:%S")
        return (f"A circle was created on {dateCreated}\n"
                f"Color of circle is {self.getColor()}\n"
                f"Filled: {self.isFilled()}\n"
                f"The radius is {self.__radius}\n"
                f"The area is {area}\n"
                f"The perimeter is {perimeter}")

class Rectangle(GeometricObject):
    def __init__(self, width=1.0, height=1.0, color='white', filled=False):
        super().__init__(color, filled)
        self.__width = width
        self.__height = height

    def getWidth(self):
        return self.__width

    def setWidth(self, width):
        self.__width = width

    def getHeight(self):
        return self.__height

    def setHeight(self, height):
        self.__height = height

    def getArea(self):
        return self.__width * self.__height

    def getPerimeter(self):
        return 2 * (self.__width + self.__height)

    def __str__(self):
        area = self.getArea()
        perimeter = self.getPerimeter()
        dateCreated = self.getDateCreated().strftime("%Y-%m-%d %H:%M:%S")
        return (f"A rectangle was created on {dateCreated}\n"
                f"Color of rectangle is {self.getColor()}\n"
                f"Filled: {self.isFilled()}\n"
                f"The width is {self.__width}\n"
                f"The height is {self.__height}\n"
                f"The area is {area}\n"
                f"The perimeter is {perimeter}")

def main():
    radius = float(input("Enter the radius of your circle: "))
    circle = Circle(radius, color='blue', filled=True)
    print()
    print(circle)
    rectangle = Rectangle(4.0, 2.0, color='red', filled=False)
    print()
    print(rectangle)

if __name__ == '__main__':
    main()
