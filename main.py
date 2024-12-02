class ListNode:
    def __init__(self, val) -> None:
        self.value = val
        self.next = None

class List:
    def __init__(self) -> None:
        self.root = None
    
    # O(1)
    def insert_front(self, val):
        new_node = ListNode(val)
        new_node.next = self.root
        self.root = new_node

    def insert_back(self, val):
        pass
    
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
l.print()
sz1 = l.size()
print(sz1)
l.insert_front(3)
l.insert_front(5)
l.insert_front(7)
sz2 = l.size()
print(sz2)

f5 = l.find(5)
print(f5)
f15 = l.find(15)
print(f15)

l.insert_back(15)
l.print()
