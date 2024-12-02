class ListNode:
    def __init__(self, val) -> None:
        self.value = val
        self.next = None
    
    def insert_back_recursive(self, val):
        if self.next:
            self.next.insert_back_recursive(val)
        else:
            self.next = ListNode(val)

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

    
    def size(self):
        pass

    def find(self, val):
        pass

    def print(self):
        pass

    def remove_front(self):
        if self.root != None:
            self.root = self.root.next

l = List()
l.insert_front(3)
l.insert_front(5)
l.insert_back(15)
