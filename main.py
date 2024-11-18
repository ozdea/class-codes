class Array:
    # O(1)
    def __init__(self):
        self.count = 0
        self.start = None

    # O(1)
    def size(self):
        return self.count

    # O(n)
    def insert(self, val):
        if self.start is None:
            self.start = [None] * 1
            self.start[0] = val
            self.count = 1
        else:
            new_count = self.count + 1
            new_start = [None] * new_count
            for i in range(self.count):
                new_start[i] = self.start[i]
            new_start[new_count - 1] = val
            self.count = new_count
            self.start = new_start

    # O(n)
    def insert_front(self, val):
        if self.start is None:
            self.start = [None] * 1
            self.start[0] = val
            self.count = 1
        else:
            new_count = self.count + 1
            new_start = [None] * new_count
            for i in range(self.count):
                new_start[i+1] = self.start[i]
            new_start[0] = val
            self.count = new_count
            self.start = new_start


    # corresponds to the in operator in Python
    # O(n) -> linear search
    def find(self, val):
        if self.count == 0:
            return False
        else:
            for i in range(self.count):
                if self.start[i] == val:
                    return True
            return False

arr = Array()
sz1 = arr.size()
arr.insert(4)
sz2 = arr.size()
arr.insert(7)
sz3 = arr.size()
arr.insert(9)
sz4 = arr.size()

find1 = arr.find(7)
find2 = arr.find(19)

i = 5

# Python str can be interpreted as an array of characters
# with similar algorithmic complexity associated with the functions