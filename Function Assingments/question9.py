# Define a function in such a way that it can accept n number of values and print their sum.
# [ variable number of arguments]

def sum(*num):
    total=0
    for i in num:
        total+=i
    return total
user_numbers=input("Enter numbers you want to add seperated with space ").split()
num=[int(x) for x in user_numbers]
total_sum=sum(*num)
print("sum of ",num," is ",total_sum)
