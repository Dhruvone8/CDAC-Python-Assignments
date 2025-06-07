# Accept 5 students name and store them in the dictionary by providing keys from 1 to 5 respectively.

students = {}

for i in range(1, 6):
    name = input(f"Enter name of student {i}: ")
    students[i] = name

print("\nStudent Dictionary:")
print(students)
