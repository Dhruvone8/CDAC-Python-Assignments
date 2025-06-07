# Note: use List comprehension
# Create a list with the numbers from 1 to 20
# Create one more list which should contain only odd numbers from the first list.

numbers = []

for i in range(1, 21):
    numbers.append(i)

comp_list = [num for num in numbers if num % 2 != 0]

print("All numbers:", numbers)
print("Odd numbers:", comp_list)
