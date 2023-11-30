class Array:
    def __init__(self) -> None:
        self.size = 0
        self.array = None
    
    def insert(self, value):
        # allocate new array
        new_size = self.size + 1
        new_array = [None] * new_size

        # copy existing elements to the new array
        for i in range(self.size):
            new_array[i] = self.array[i]

        #insert the new item at the end
        new_array[self.size] = value

        # update attributes 
        self.size = new_size
        self.array = new_array


my_array = Array()
my_array.insert(3)
my_array.insert(5)
my_array.insert(6)

