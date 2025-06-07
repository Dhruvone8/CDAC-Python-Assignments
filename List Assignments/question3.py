# Accept 5 numbers, store them inside the list & display it.
# Now add 3 more numbers [hardcoded] at the end of the list using "extend" method.

numbers = []

for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("Original List:", numbers)

numbers.extend([100, 200, 300])

print("Final List:", numbers)
