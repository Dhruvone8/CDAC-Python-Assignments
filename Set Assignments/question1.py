# Accept 10 values from user and add them inside the set.
# Now accept one more value from user and if it is present in the set, remove it.
# Make sure program doesn't give any error if number is not there inside the set.

nums = set()

for i in range(10):
    val = int(input("Enter a number: "))
    nums.add(val)

print("Current Set:", nums)

r = int(input("Enter a value: "))

nums.discard(r)

# Display the updated set
print("Updated Set:", nums)
