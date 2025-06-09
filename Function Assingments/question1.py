# #1) define 3 functions "add()","modify()" and "delete()" with just a print message.
# now accept input from user as a number. if the number entered is 1, call "add()"
# if it is 2, call "modify()" if it is 3, call "delete()" [ hint: use "match... case" ]


def add():
     print("This is add function")
def modify():
    print("This is modify fun")
def delete():
    print("Delete function ")

choice=input("1: Add\t2:Modify\t3:Delete ")
match choice:
    case "1":
        add()
    case "2":
        modify()
    case "3":
        delete()
    case _:
      print("You didnt respond 1-3")

