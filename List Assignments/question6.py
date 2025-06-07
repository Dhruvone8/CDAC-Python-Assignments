# Accept 5 numbers, store them inside the list.
# Now accept a position from user ,remove the element from that position
# After removing it, display the list.

numbers = []

for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

remove_index = int(input("Enter the position of the number you want to remove: "))
numbers.remove(numbers[remove_index - 1])
print(numbers)