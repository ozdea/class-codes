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

    def size_recursive(self):
        left_size = 0
        if self.left:
            left_size = self.left.size_recursive()

        right_size = 0
        if self.right:
            right_size = self.right.size_recursive()

        return 1 + left_size + right_size

    def find_recursive(self, val):
        if val == self.value:
            return True
        elif val < self.value:
            if self.left:
                return self.left.find_recursive(val)
            else:
                return False
        else:
            if self.right:
                return self.right.find_recursive(val)
            else:
                return False


class Tree:
    def __init__(self) -> None:
        self.root = None
    
    # O(n)
    def insert(self, val):
        if self.root == None:
            self.root = TreeNode(val)
        else:
            self.root.insert_recursive(val)
    
    # O(n)
    def size(self):
        if self.root == None:
            return 0
        else:
            return self.root.size_recursive()
    
    # O(log n)
    def find(self, val):
        if self.root == None:
            return False
        else:
            return self.root.find_recursive(val)
    
    # O(log n)
    def find_iterative(self, val):
        current_node = self.root
        while current_node:
            if val == current_node.value:
                return True
            elif val < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False

t = Tree()
t.insert(3)
t.insert(10)
t.insert(1)
sz = t.size()
print(sz)

t.insert(15)
t.insert(8)
t.insert(2)
sz2 = t.size()
print(sz2)

f1 = t.find(8)
print(f1)

f2 = t.find(0)
print(f2)

f3 = t.find_iterative(8)
print(f3)
