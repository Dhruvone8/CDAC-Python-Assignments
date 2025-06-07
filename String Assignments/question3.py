# Accept a string and display how many vowel characters are there inside it.

s = input("Enter a string: ")
lower_s = s.lower()
count = 0

for char in lower_s:
    if char in ['a', 'e', 'i', 'o', 'u']:
        count += 1

print(f'There are {count} vowels in this string.')
