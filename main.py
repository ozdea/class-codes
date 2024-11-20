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
    
    # O(n)
    def size(self):
        count = 0
        current_node = self.root
        while current_node != None:
            count += 1
            current_node = current_node.next
        return count

l = List()
sz1 = l.size()
print(sz1)
l.insert_front(3)
l.insert_front(5)
l.insert_front(7)
sz2 = l.size()
print(sz2)
