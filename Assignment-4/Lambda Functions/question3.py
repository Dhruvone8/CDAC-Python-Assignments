# Write a function with 2 arguments, second argument should be "default argument" and display them. Using
# 	a) normal function
# 	b) lambda

def func(num, a = 5):
    return a * num
print(func(4))

func1 = lambda num, a = 5: num * a
print(func1(5))
