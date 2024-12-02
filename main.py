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
    def insert_back(self, val):
        if self.root == None:
            self.insert_front(val)
        else:
            current_node = self.root
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = ListNode(val)
    
    # O(n)
    def size(self):
        count = 0
        current_node = self.root
        while current_node != None:
            count += 1
            current_node = current_node.next
        return count

    # O(n)
    def find(self, val):
        current_node = self.root
        while current_node != None:
            if current_node.value == val:
                return True
            current_node = current_node.next
        return False

    # O(n)
    def print(self):
        print("[", end="")
        current_node = self.root
        while current_node != None:
            print(current_node.value, end=" ")
            current_node = current_node.next
        print("]")

    # O(1)
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
