# Accept 5 names and store them in list.
# Now sort the list in ascending order display and then in descending order.

names = []

for i in range(5):
    name = input(f"Enter name {i+1}: ")
    names.append(name)

# Sort in ascending order
ascending = sorted(names)

# Sort in descending order
descending = sorted(names, reverse=True)

# Display results
print("List in ascending order:", ascending)
print("List in descending order:", descending)
