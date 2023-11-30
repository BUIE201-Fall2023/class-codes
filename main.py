class Array:
    def __init__(self) -> None:
        self.size = 0
        self.array = None
    
    # O(n)
    def insert(self, value):
        # allocate new array O(1)
        new_size = self.size + 1
        new_array = [None] * new_size

        # copy existing elements to the new array O(n)
        for i in range(self.size):
            new_array[i] = self.array[i]

        #insert the new item at the end O(1)
        new_array[self.size] = value

        # update attributes O(1)
        self.size = new_size
        self.array = new_array

    # O(n)
    def insert_front(self, value):
        # allocate new array
        new_size = self.size + 1
        new_array = [None] * new_size

        # copy existing elements to the new array
        for i in range(self.size):
            new_array[i + 1] = self.array[i]

        #insert the new item at the beginning
        new_array[0] = value

        # update attributes 
        self.size = new_size
        self.array = new_array

    # O(n)
    # A possible implementation of Python in operator 
    def find(self, value):
        for i in range(self.size):
            if self.array[i] == value:
                return True
        return False
    
    # O(1)
    def count(self):
        return self.size

my_array = Array()
my_array.insert(3)
my_array.insert(5)
my_array.insert(6)

result6 = my_array.find(6)
result8 = my_array.find(8)

size = my_array.count()

# string is an array of characters with similar complexity operations
