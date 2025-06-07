# Accept a string and display it.
# Now accept slicing positions from and to ,slice the string and display it.

s = input("Enter a string: ")
print(s)

a = int(input("From where do you want to start the string: "))
b = int(input("Till which position you want the string to be printed: "))

print(s[a-1:b])