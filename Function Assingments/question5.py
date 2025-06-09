# Define a function to accept a number.
# This function should return 1 if a number passed is more than 0
# Return -1 if a number passed is less than 0 ,else it should return 0

def check(number):
    if(number>0):
        return 1
    elif(number<0):
        return -1
    else:
        return 0

number=int(input("Enter a number"))
print(check(number))
