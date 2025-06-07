# Accept 5 numbers, store them inside the list.
# Now accept a number from user which he would like to remove from the list
# After removing it, display the list.

numbers = []

for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

remove_number = int(input("Enter a number you want to remove from the list: "))
numbers.remove(remove_number)
print(numbers)