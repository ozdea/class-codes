class ListNode:
    def __init__(self, val) -> None:
        self.value = val
        self.next = None
    
    def insert_back_recursive(self, val):
        if self.next:
            self.next.insert_back_recursive(val)
        else:
            self.next = ListNode(val)

    def size_recursive(self):
        if self.next:
            return 1 + self.next.size_recursive()
        else:
            return 1
    
    def find_recursive(self, val):
        if self.value == val:
            return True
        elif self.next == None:
            return False
        else:
            return self.next.find_recursive(val)
    
    def print_recursive(self):
        print(self.value, end=" ")
        if self.next:
            self.next.print_recursive()

    def print_backward_recursive(self):
        if self.next:
            self.next.print_backward_recursive()
        print(self.value, end=" ")

class List:
    def __init__(self) -> None:
        self.root = None
    
    # O(1)
    def insert_front(self, val):
        new_node = ListNode(val)
        new_node.next = self.root
        self.root = new_node

    # O(n)
    def insert_back(self, val):
        if self.root:
            self.root.insert_back_recursive(val)
        else:
            self.insert_front(val)

    # O(n)
    def size(self):
        if self.root:
            return self.root.size_recursive()
        else:
            return 0

    # O(n)
    def find(self, val):
        if self.root:
            return self.root.find_recursive(val)
        else:
            return False

    def print(self):
        print("[", end="")
        if self.root:
            self.root.print_recursive()
        print("]")

    def print_backward(self):
        print("[", end="")
        if self.root:
            self.root.print_backward_recursive()
        print("]")


    def remove_front(self):
        if self.root != None:
            self.root = self.root.next

l = List()
sz1 = l.size()
print(sz1)
l.insert_front(3)
l.insert_front(5)
l.insert_back(15)
sz2 = l.size()
print(sz2)

f1 = l.find(15)
print(f1)

f2 = l.find(0)
print(f2)

l.print()