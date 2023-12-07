class ListNode:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
    
    def insert_end_recursive(self, value):
        if self.next == None:
            self.next = ListNode(value)
        else:
            self.next.insert_end_recursive(value)
    
    def count_recursive(self):
        if self.next == None:
            return 1
        else:
            return 1 + self.next.count_recursive()
        
    def find_recursive(self, value):
        if self.value == value:
            return True
        elif self.next == None:
            return False
        else:
            return self.next.find_recursive(value)

class LinkedList:
    def __init__(self) -> None:
        self.root = None

    def insert_front(self, value):
        new_node = ListNode(value)
        new_node.next = self.root
        self.root = new_node

    def insert_end(self, value):
        if self.root == None:
            self.root = ListNode(value)
        else:
            self.root.insert_end_recursive(value)

    def count(self):
        if self.root == None:
            return 0
        else:
            return self.root.count_recursive()

    def find(self, value):
        if self.root == None:
            return False
        else:
            return self.root.find_recursive(value)
    
    def get_index(self, index):
        pass
        
    def print(self):
        pass

l = LinkedList()

l.insert_front(3)
l.insert_front(6)
l.insert_front(10)

l.insert_end(15)

count = l.count()

find3 = l.find(3)

find5 = l.find(5)

# index2 = l.get_index(2)

# l.print()

i = 4