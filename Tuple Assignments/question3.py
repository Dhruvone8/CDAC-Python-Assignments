# Write a Python program to find the repeated items of a tuple.

tuple = (1, 3, 5, 3, 7, 9, 1, 3, 9, 11)

repeated = set()

for item in tuple:
    if tuple.count(item) > 1:
        repeated.add(item)

print("Repeated items in the tuple:", repeated)
