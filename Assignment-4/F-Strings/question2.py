# Ask the user for the item name, quantity, and price per item. Use an f-string to display:
# "You bought <quantity> <item_name>(s) at ₹<price> each. Total cost is ₹<total>."

name = input("Enter name of the item: ")
quantity = int(input("Enter quantity of items: "))
price = int(input("Enter price of items: "))

print(f"You bought {quantity} {name} at ₹{price} each. Total Cost is {price * quantity}")
