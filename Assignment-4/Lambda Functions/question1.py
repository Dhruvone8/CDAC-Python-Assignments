# Write a function to accept a number and return its square using
    # 	a) normal function
    # 	b) lambda

def square(num):
    return num * num

print(f"Square of a number using normal function: {square(5)}")

square = lambda num: num * num
print(f"Square of a number using lambda: {square(5)}")
