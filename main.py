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


l = [1, 3, 7, 13, 18, 50, 75, 80, 99]

f1 = binary_search(l, 75)
print(f1)

f2 = binary_search(l, 15)
print(f2)