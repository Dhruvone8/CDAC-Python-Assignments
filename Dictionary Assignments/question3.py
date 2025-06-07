# Given a dictionary of students and their favourite colours:
# people = {'Arham':'Blue','Lisa':'Yellow',''Vinod:'Purple','Jenny':'Pink'}
    # 1. Find out how many students are in the list
    # 2. Change Lisa’s favourite colour
    # 3. Remove 'Jenny' and her favourite color
    # 4. Sort and print students and their favourite colours alphabetically by name

people = {'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}

# Number of students
print("Number of students: ", len(people))

# Change Lisa's Fav Color
people['Lisa'] = 'Orange'

# Remove Jenny
people.pop('Jenny')

# Sort
for student in sorted(people.keys()):
    print(f"{student}: {people[student]}")
