# Accept a string and display whether it is palindrome or not.

s = input("Enter a string: ")

if s == s[::-1]:
    print(f'"{s}" is a palindrome.')
else:
    print(f'"{s}" is not a palindrome.')
