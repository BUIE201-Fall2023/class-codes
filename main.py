class ListNode:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.root = None

    # O(1)
    def insert_front(self, value):
        if self.root == None:
            self.root = ListNode(value)
        else:
            new_node = ListNode(value)
            new_node.next = self.root
            self.root = new_node

    # O(n)
    def insert_end(self, value):
        if self.root == None:
            self.root = ListNode(value)
        else:
            # find the last node
            current_node = self.root
            while current_node.next:
                current_node = current_node.next
            # insert a new node at the end
            current_node.next = ListNode(value)

    # O(n)
    def count(self):
        if self.root == None:
            return 0
        else:
            i = 0
            current_node = self.root
            while current_node:
                i += 1
                current_node = current_node.next
            return i

    # O(n)    
    def find(self, value):
        if self.root == None:
            return None
        else:
            current_node = self.root
            while current_node:
                if current_node.value == value:
                    return current_node
                else:
                    current_node = current_node.next
            return None

l = LinkedList()
count = l.count()

l.insert_front(3)
l.insert_front(6)
l.insert_front(10)

l.insert_end(15)

count = l.count()

find3 = l.find(3)

find5 = l.find(5)

