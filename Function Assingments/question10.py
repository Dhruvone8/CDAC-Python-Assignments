# Create 3 functions "show1()","show2()" and "show3()"
# Now define a function "caller" that can accept any function as an argument and invoke the same.

def show1():
    print("Inside show 1")

def show2():
    print("Inside show 2")
def show3():
    print("Inside show 3")

def caller(func):
    if(callable(func)):
        func()

caller(show1)
caller(show2)
caller(show3)
