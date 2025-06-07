# Create empty list, accept numbers till user enters 0 and store them inside the list.
# Print the list and its length.

numbers = []

n = int(input("Enter a number: "))

while n != 0:
    numbers.append(n)
    n = int(input("Enter a number: "))

print("List:", numbers)
print("Length of the List:", len(numbers))

