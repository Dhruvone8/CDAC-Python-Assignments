# Define "myfun1()" with a print statement. now define "myfun2()" which should invoke "myfun1()" function.

def myfun1():
    print("Inside myfun 1")

def myfun2():
    myfun1()
myfun2()