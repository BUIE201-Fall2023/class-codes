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