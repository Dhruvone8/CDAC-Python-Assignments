# Accept a number, string, decimal, boolean value and a character from the user
# Store it inside the list. First print the list from the beginning and then from the end.

list = []

number = int(input("Enter a number: "))
name = input("Enter a string: ")
decimal = float(input("Enter a decimal: "))
boolean = bool(input("Enter a boolean value: "))
character = input("Enter a character: ")

list.append(number)
list.append(name)
list.append(decimal)
list.append(boolean)
list.append(character)

print("List from beginning: ", list)
print("List from end: ", list[::-1])
