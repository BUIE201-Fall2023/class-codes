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
        
    def print_recursive(self):
        print(self.value, " ", end="")
        if self.next:
            self.next.print_recursive()

    def print_recursive_backward(self):
        if self.next:
            self.next.print_recursive_backward()
        print(self.value, " ", end="")

    def sum_recursive(self):
        if self.next:
            return self.value + self.next.sum_recursive()
        else:
            return self.value

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
    
    def print(self):
        if self.root == None:
            print("[]")
        else:
            print("[", end="")
            self.root.print_recursive()
            print("]")

    def print_backward(self):
        if self.root == None:
            print("[]")
        else:
            print("[", end="")
            self.root.print_recursive_backward()
            print("]")

    def sum_iterative(self):
        total = 0
        current_node = self.root
        while current_node:
            total += current_node.value
            current_node = current_node.next
        return total

    def sum_recursive(self):
        if self.root == None:
            return 0
        else:
            return self.root.sum_recursive()

l = LinkedList()

l.insert_front(3)
l.insert_front(6)
l.insert_front(10)

l.insert_end(15)

count = l.count()

find3 = l.find(3)

find5 = l.find(5)

l.print()
l.print_backward()

result = l.sum_iterative()
result2 = l.sum_recursive()

i = 4