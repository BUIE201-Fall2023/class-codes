class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

    # O(log n)
    def insert_recursive(self, value):
        if value <= self.value:
            if self.left == None:
                self.left = TreeNode(value)
            else:
                self.left.insert_recursive(value)
        else:
            if self.right == None:
                self.right = TreeNode(value)
            else:
                self.right.insert_recursive(value)
    
    # O(log n)
    def find_recursive(self, value):
        if value == self.value:
            return True
        elif value < self.value:
            if self.left == None:
                return False
            else:
                return self.left.find_recursive(value)
        else:
            if self.right == None:
                return False
            else:
                return self.right.find_recursive(value)
    
    def count_recursive(self):
        left_count = 0
        if self.left:
            left_count = self.left.count_recursive()
        right_count = 0
        if self.right:
            right_count = self.right.count_recursive()

        return 1 + left_count + right_count
class Tree:
    def __init__(self) -> None:
        self.root = None
    
    # O(log n)
    def insert(self, value):
        if self.root == None:
            self.root = TreeNode(value)
        else:
            self.root.insert_recursive(value)

    # O(log n)  
    def find(self, value):
        if self.root == None:
            return False
        else:
            return self.root.find_recursive(value)

    # O(n)  
    def count(self):
        if self.root == None:
            return 0
        else:
            return self.root.count_recursive()

t = Tree()
t.insert(10)
t.insert(15)
t.insert(5)
t.insert(13)
t.insert(3)
t.insert(8)

r = t.find(8)
r2 = t.find(20)

n = t.count()

i = 4