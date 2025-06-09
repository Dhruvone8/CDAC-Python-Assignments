# Define a function which accepts character,int,string and display them.

def accept(a,b,c):
    print("The character given is ",a)
    print("The int number given is ", b)
    print("String given is: ",c)


a=input("Enter a character: ")
b=int(input("Enter a Number: "))
c=input("Enter a String: ")
if(type(a) == str and len(a) == 1 and type(b) == int and type(c) == str):
    accept(a,b,c)