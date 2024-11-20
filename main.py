class ListNode:
    def __init__(self, val) -> None:
        self.value = val
        self.next = None

class List:
    def __init__(self) -> None:
        self.root = None
    
    def insert_front(self, val):
        new_node = ListNode(val)
        new_node.next = self.root
        self.root = new_node

l = List()
l.insert_front(3)
l.insert_front(5)
l.insert_front(7)
