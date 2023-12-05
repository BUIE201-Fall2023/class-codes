class Array:
    def __init__(self) -> None:
        self.size = 0
        self.array = None
    
    # O(n)
    def insert(self, value):
        # CODE REQUIRED
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
    
    def contains(self, other):
        if self.size >= other.size:
            for i in range (self.size - other.size + 1):
                all_same = True
                for j in range (other.size):
                    if self.array[i + j] != other.array[j]:
                        all_same = False
                        break
                if all_same:
                    return True
        return False


my_array = Array()
my_array.insert(4)
my_array.insert(5)
my_array.insert(2)
my_array.insert(1)

other = Array()
other.insert(2)
other.insert(1)

result1 = my_array.contains(other)

other2 = Array()
other2.insert(1)
other2.insert(2)

result2 = my_array.contains(other2)
