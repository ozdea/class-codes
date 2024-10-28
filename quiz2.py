import time

def check_duplicate(check):
    for i in range(len(check) - 1):
        for j in range(i + 1, len(check)):
            if check[i] == check[j]:
                return check[i]
    return None

check = [1, -5, 4, 7, -5, 5]
result1 = check_duplicate(check)
print(result1)

result2 = check_duplicate([])
print(result2)

check = [1, -2, 4, 7, -3, 5]
result3 = check_duplicate(check)
print(result3)

def check_set(check):
    already_seen = set()
    for number in check:
        if number in already_seen:
            return number
        else:
            already_seen.add(number)
    return None

check = [1, -5, 4, 7, -5, 5]
result1 = check_set(check)
print(result1)

result2 = check_set([])
print(result2)

check = [1, -2, 4, 7, -3, 5]
result3 = check_set(check)
print(result3)

n = 50
check = list(range(n))

start = time.time()
result = check_set(check)
end = time.time()
print("check_set time: ", end - start)

start = time.time()
result = check_duplicate(check)
end = time.time()
print("check_duplicate time: ", end - start)

def check_max_duplicate(check):
    item_counts = {}
    for i in check:
        if i in item_counts:
            item_counts[i] += 1
        else:
            item_counts[i] = 1
    
    max_item = None
    for i in item_counts:
        if item_counts[i] > 1:
            if max_item is None or item_counts[i] > item_counts[max_item]:
                max_item = i
    return max_item

l = [2, 5, -1, 8, -1, 5, 2, -1]
result = check_max_duplicate(l)
print(result)
