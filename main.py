class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def print(self):
        for i in range(self.height):
            for j in range(self.width):
                print("*", end="")
            print("")

r = Rectangle(3, 5)
r.print()

class Square:
    def __init__(self, dimension) -> None:
        self.dimension = dimension
    
    def print(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                print("*", end="")
            print("")

s = Square(4)
s.print()

class NewSquare(Rectangle):
    def __init__(self, dimension):
        super().__init__(dimension, dimension)
        # violates data encapsulation
        # self.height = dimension
        # self.width = dimension

ns = NewSquare(7)
ns.print()