i = hash("caner")
print(i)

class HashTable:
    def __init__(self) -> None:
        self.BUCKET_SIZE = 100
        self.buckets = [None] * self.BUCKET_SIZE

    # O(1) on average
    def insert(self, value):
        hashed_value = hash(value)
        index = hashed_value % self.BUCKET_SIZE
        if self.buckets[index] is None:
            self.buckets[index] = []
        self.buckets[index].append(value)
    
    # O(1) on average
    def find(self, value):
        hashed_value = hash(value)
        index = hashed_value % self.BUCKET_SIZE

        if self.buckets[index] is None:
            return False
        else:
            return value in self.buckets[index]

# Python set and dictionary are based on hash tables
        
h = HashTable()
h.insert("caner")
h.insert("tamer")
h.insert("tınaz")

find1 = h.find("caner")
find2 = h.find("mustafa")

i = 5