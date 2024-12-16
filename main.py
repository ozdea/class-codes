names = ["caner", "tinaz", "mustafa", "aybek"]
print(names)

# common but O(n^2) in the worst case
capitalized = []
for name in names:
    capitalized.append(name.capitalize())
print(capitalized)

# O(n) 
n = len(names)
capitalized2 = [None] * n
for i in range(n):
    capitalized2[i] = names[i].capitalize()
print(capitalized2)

# List comprehension O(n)
capitalized3 = [name.capitalize() for name in names]
print(capitalized3)

# set comprehension
capitalized_set = {name.capitalize() for name in names}
print(capitalized_set)

capitalized_dict = {name: name.capitalize() for name in names}
print(capitalized_dict)

numbers = [1, 4, -3, -5, 10]
print(numbers)
abs_numbers = [abs(number) for number in numbers]
print(abs_numbers)
