class Rectangle:
    def __init__(self, Height, Width) -> None:
        self.Height = Height
        self.Width = Width
    
    def print(self):
        for i in range(self.Height):
            for j in range(self.Width):
                print("*", end="")
            print()

r = Rectangle(5, 7)
r.print()
# Rectangle.print(r) # equivalent to the previous call

class Square:
    def __init__(self, dimension) -> None:
        self.dimension = dimension

    def print(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                print("*", end="")
            print()

s = Square(3)
s.print()

class NewSquare(Rectangle):
    def __init__(self, dimension, additional_field = 5) -> None:
        super().__init__(dimension, dimension)
        self.my_additional_field = additional_field
        # violates data encapsulation
        # self.Height = dimension
        # self.Width = dimension
    
    def my_additional_function(self):
        print("NewSquare.my_additional_function was called ", self.my_additional_field)

    # function override
    def print(self):
        print("NewSquare.print() was called")
        super().print()

ns = NewSquare(8)
ns.print()
ns.my_additional_function()

i = 5

