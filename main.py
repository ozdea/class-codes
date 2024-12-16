# O(log n)
def binary_search(l, val):
    left = 0
    right = len(l) - 1
    while left <= right:
        mid = (left + right) // 2
        if l[mid] == val:
            return True
        elif l[mid] < val:
            left = mid + 1
        else:
            right = mid - 1
    return False

def binary_search_recursive(l, val, left, right):
    if left > right:
        return False
    mid = (left + right) // 2
    if l[mid] == val:
        return True
    elif l[mid] < val:
        return binary_search_recursive(l, val, mid + 1, right)
    else:
        return binary_search_recursive(l, val, left, mid - 1)    

l = [1, 3, 7, 13, 18, 50, 75, 80, 99]

f1 = binary_search(l, 75)
print(f1)

f2 = binary_search(l, 15)
print(f2)

f3 = binary_search_recursive(l, 75, 0, len(l) - 1)
print(f3)

f4 = binary_search_recursive(l, 15, 0, len(l) - 1)
print(f4)
