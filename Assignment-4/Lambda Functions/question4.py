# Write a function with variable no. of arguments and display them. Using
# 	normal function
# 	lambda

def func(*a):
    return sum(a)

print(func(51, 30, 1))