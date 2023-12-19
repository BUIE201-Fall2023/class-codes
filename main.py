class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

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

class Tree:
    def __init__(self) -> None:
        self.root = None
    
    # O(log n)
    def insert(self, value):
        if self.root == None:
            self.root = TreeNode(value)
        else:
            self.root.insert_recursive(value)

t = Tree()
t.insert(10)
t.insert(15)
t.insert(5)
t.insert(13)
t.insert(3)
t.insert(8)

