import sys

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
    def __init__(self, dimension, name):
        super().__init__(dimension, dimension)
        # violates data encapsulation
        # self.height = dimension
        # self.width = dimension
        self.name = name

    def hello(self):
        print(f"Hello from NewSquare called: {self.name}")

    # function override
    def print(self):
        print("Printing NewSquare called: ", self.name)
        super().print()
        # violates data encapsulation
        # for i in range(self.width):
        #     for j in range(self.height):
        #         print("*", end="")
        #     print("")


ns = NewSquare(7, "ns")
ns.print()
ns.hello()

# everything is object in python

print("issubclass(NewSquare, Rectangle)", issubclass(NewSquare, Rectangle))
print("issubclass(Square, Rectangle)", issubclass(Square, Rectangle))

print("issubclass(Square, object)", issubclass(Square, object))
print("issubclass(int, object)", issubclass(int, object))

print("issubclass(int, float)", issubclass(int, float))

print("issubclass(bool, int)", issubclass(bool, int))
