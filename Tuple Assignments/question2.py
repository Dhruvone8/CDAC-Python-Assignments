# Create a tuple to store 5 numbers and then sort it in ascending and descending order.

numbers = (38, 57, 48, 63, 45)

num_list = list(numbers)

asc_sorted = tuple(sorted(num_list))
print("Ascending order:", asc_sorted)

desc_sorted = tuple(sorted(num_list, reverse=True))
print("Descending order:", desc_sorted)




