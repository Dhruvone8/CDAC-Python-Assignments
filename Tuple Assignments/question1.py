# Python program to count the elements in a list until an element is a tuple.

my_list = [1, "apple", 3.14, [2, 3], (5, 6), "python"]

count = 0

for item in my_list:
    if type(item) == tuple:
        break
    count += 1

print("Number of elements before tuple:", count)
