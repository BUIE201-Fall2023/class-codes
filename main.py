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

l = LinkedList()
count = l.count()

l.insert_front(3)
l.insert_front(6)
l.insert_front(10)

count = l.count()

