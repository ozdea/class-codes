class HashTable:
    def __init__(self) -> None:
        self.BUCKET_SIZE = 100
        self.table = [None] * self.BUCKET_SIZE
    
    # O(1) on average
    def insert(self, val):
        hashed_value = hash(val)
        index = hashed_value % self.BUCKET_SIZE
        if self.table[index] == None:
            self.table[index] = []
        self.table[index].append(val)

    # O(1)
    def find(self, val):
        hashed_value = hash(val)
        index = hashed_value % self.BUCKET_SIZE
        if self.table[index] == None:
            return False
        else:
            return val in self.table[index]

    # O(n)    
    def size(self):
        total = 0
        for l in self.table:
            if l:
                total += len(l)
        return total

h = HashTable()
h.insert("caner")
h.insert("tamer")
h.insert("tınaz")
h.insert("aybek")

f1 = h.find("caner")
f2 = h.find("refik")

s = h.size()

i = hash("caner")
j = hash(45353)

k = hash("Caner")

print(i)
print(k)

# Python set and dict are implemented as hash tables
s = set(["caner", "aybek"])

l = 3