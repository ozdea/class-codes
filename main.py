class TreeNode:
    def __init__(self, val) -> None:
        self.value = val
        self.left = None
        self.right = None
    
    def insert_recursive(self, val):
        if val < self.value:
            if self.left:
                self.left.insert_recursive(val)
            else:
                self.left = TreeNode(val)
        else:
            if self.right:
                self.right.insert_recursive(val)
            else:
                self.right = TreeNode(val)


class Tree:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, val):
        if self.root == None:
            self.root = TreeNode(val)
        else:
            self.root.insert_recursive(val)

t = Tree()
t.insert(3)
t.insert(10)
t.insert(1)
t.insert(15)
t.insert(8)
t.insert(2)
