# Create a list and store string, number, character, boolean, decimal values inside it.
# Now slice it in following ways:
    # a) display it in reverse order
    # b) list all the elements from 2nd position
    # c) list the elements from 1st to 3rd position
    # d) slice it from 1st to 3rd elements from the end.

data = []

s = input("Enter a string: ")
n = int(input("Enter a number: "))
c = input("Enter a character: ")
b = bool(input("Enter a boolean value: "))
d = float(input("Enter a decimal number: "))

data.append(s)
data.append(n)
data.append(c)
data.append(b)
data.append(d)

# In reverse order
print("List in reverse order: ", data[::-1])

# All elements from second position
print("List elements from second position: ", data[1:])

# Elements from 1st to 3rd position
print("List elements from 1st to 3rd position: ", data[:3])

# Elements from 1st to 3rd position from end
print("List elements from 1st to 3rd position from end: ", data[-1:-4:-1])




