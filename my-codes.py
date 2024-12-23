'''class TreeNode:
    def __init__(self, val) -> None:
        self.value = val
        self.left = None
        self.right = None

    def find_min_value(self):
        # Finds the minimum value in the subtree
        if self.left is None:
            return self.value
        else:
            return self.left.find_min_value()

    def remove_method(self, val):
        # Traverse the tree to find the node to remove
        if val < self.value:
            if self.left:
                self.left = self.left.remove_method(val)
        elif val > self.value:
            if self.right:
                self.right = self.right.remove_method(val)
        else:
            # Case 1: Node with no children
            if self.left is None and self.right is None:
                return None
            # Case 2: Node with only one child
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            # Case 3: Node with two children
            else:
                # Replace with the smallest value in the right subtree (in-order successor)
                min_val = self.right.find_min_value()
                self.value = min_val
                # Remove the in-order successor
                self.right = self.right.remove_method(min_val)
        return self


class Tree:
    def __init__(self) -> None:
        self.root = None

    def min_value(self):
        if self.root is None:
            return None
        else:
            return self.root.find_min_value()

    def remove(self, val):
        if self.root is None:
            return None
        else:
            self.root = self.root.remove_method(val)

t = Tree()
t.root = TreeNode(10)
t.root.left = TreeNode(5)
t.root.right = TreeNode(15)
t.root.left.left = TreeNode(3)
t.root.left.right = TreeNode(7)
t.root.right.right = TreeNode(20)
t.remove(10)


class HashTable:
    def __init__(self) -> None:
        self.BUCKET_SIZE = 100
        self.table = [None] * self.BUCKET_SIZE

    def insert(self, val):
        hashed_value = hash(val)
        index = hashed_value % self.BUCKET_SIZE
        if self.table[index] == None:
            self.table[index] = []
        self.table[index].append(val)

    def find(self, val):
        hashed_value = hash(val)
        index = hashed_value % self.BUCKET_SIZE
        if self.table[index] == None:
            return False
        return val in self.table[index]
    
    def size(self):
        total = 0
        for l in self.table:
            if l:
                total += len(l)
        return total
    

    def count_collusions(self):
        total = 0
        for l in self.table:
            if len(l) > 1:
                total += len(l) - 1 
        return total

    def load_factor(self):
        total = 0
        for l in self.table:
            if l:
                 total += len(l)
        return total / self.BUCKET_SIZE
    
    def rehash(self, val):
        if self.load_factor() > 0.75:
            self.BUCKET_SIZE = self.BUCKET_SIZE * 2
            self.table = [None] * self.BUCKET_SIZE
            hashed_value = hash(val)
            index = hashed_value % self.BUCKET_SIZE
            if self.table[index] == None:
                self.table[index] = []
            self.table[index].append(val)








h = HashTable()
h.insert("caner")
h.insert("tamer")
h.insert("tinaz")
h.insert("aybek")



def find_square_root(l, left, right, n):
    if left > right:
        return False
    else:
        mid = (left + right) // 2  
        if l[mid]  == int(n**0.5):
            return l[mid]
        elif l[mid] > int(n**0.5):  
            return find_square_root(l, left, mid -1, n)
        else: 
            return find_square_root(l, mid +1, right, n)

        
l = [i for i in range(100)]

f3 = find_square_root(l, 0, len(l) - 1, 64)
print(f3)

#chat's suggestion
def find_square_root(l, left, right, n):
    if left > right:
        return right  # When no exact match is found, return the largest valid integer
    else:
        mid = (left + right) // 2  
        if mid * mid == n:  # Compare the square of `mid` with `n`
            return mid
        elif mid * mid > n:  
            return find_square_root(l, left, mid - 1, n)
        else: 
            return find_square_root(l, mid + 1, right, n)
dict = {num: 'even' if num % 2 == 0 else 'odd' for num in range(1,11)}
print(dict)


class Array():
    def __init__(self):
        self.count = 0
        self.start = None

    def insert(self,val):
        if self.count == 0:
            self.start = [None] * 1
            self.start[0] = val
            self.count = 1
        else:
            new_count = self.count + 1
            new_start = new_count * [None]
            for i in range(self.count):
                new_start[i] = self.start[i]
            new_start[new_count-1] = val
            self.count = new_count
            self.start = new_start
        
    def remove(self,val):
        if self.count == 0:
            return False
        found = False
        new_count = self.count -1
        new_start = new_count * [None]
        for i in range(self.count):
            if self.start[i] == val:
                found = True
            else:

                for j in range(i,self.count-1):
                    new_start[j] = self.start[i+1]
                
    
                self.count = new_count
                self.start = new_start
                return self.start
        return False
    



    def remove(self, val):
        if self.count == 0:
            return False

        found = False
        for i in range(self.count):
            if self.start[i] == val:
                found = True
                for j in range(i, self.count - 1):
                    self.start[j] = self.start[j + 1]
                break

        if not found:
            return False

        self.count -= 1
        self.start[self.count] = None 
    
arr = Array()
arr.insert(1)
arr.insert(2)
arr.insert(3)
arr.insert(4)
arr.remove(3)





# Write a function that checks if two integers in a given list add up to 
# a given target
# If check = [1, -2, 4, 7, -3, 5] and target = 3, the function should return True since -2 + 5 = 3. 
# If check = [1, -2, 4, 7, -3, 5] and target = 13, the function should return False since no pair of elements add to 13. 

# a) Implement the function so that you iterate through each pair of integers without using any additional data structures
# b)	Implement the function so that you make a single pass through the list (i.e. each element is considered only once). You may create additional data structures such as dict. 



def check_add(check, target):
    for i in range(len(check)):
        for j in range(i+1,len(check)):
            if check[i] + check[j] == target:
                return True
            
    return False
check = [1, -2, 4, 7, -3, 5, 5]

print(check_add(check, 10))


def check_add_set(check, target):
    seen = set()
    for num in check:
        if target - num in seen:  # Check for complement in `seen`
            return True
        seen.add(num)  # Add the current number to `seen`
    return False
print(check_add_set(check, 10))
'''


# consider the HashTable that we have implemented in class. 
# implement find function 

class HashTable:
    def __init__(self) -> None:
        self._bucket_size = 100
        self._array = [None] * self._bucket_size
    
    def insert(self, value):
        hash_value = hash(value)
        index = hash_value % self._bucket_size
        if self._array[index] == None:
            self._array[index] = []
        self._array[index].append(value)

    def find(self, value):
        hash_value = hash(value)
        index = hash_value % self._bucket_size
        if self._array[index] == value:
            return True
        return False


        
     
h = HashTable()
h.insert("IE 201")
h.insert("IE 203")
h.insert("IE 515")

print(h.find("IE 201")) # should print True
print(h.find("IE 613")) # should print False


def print_date(date):
    print("The date printed using print_date is {}/{}/{}".format(date.Day, date.Month, date.Year))