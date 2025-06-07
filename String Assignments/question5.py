# Accept a string and find out how many words are there in it

s = input("Enter the string: ")

words = s.split()

num_words = len(words)

print(f"Number of words in the string are: {num_words}")
