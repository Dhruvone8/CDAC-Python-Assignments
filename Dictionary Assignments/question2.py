# create a dictionary with pairs
    # 	soap:100
    # 	deo:300
    # 	perfume:400

products = {"soap": 100, "deo": 300, "perfume" : 400}

print(products)

user_input = input("Enter the product name: ")

if user_input in products:
    print(f"Price of {user_input} is {products[user_input]} rupees")
else:
    print("product not available")
