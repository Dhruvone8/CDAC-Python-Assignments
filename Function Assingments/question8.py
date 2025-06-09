# Write a function to accept minimum 3 characters and maximum 5 characters.

def defaultfun(value="abc"):
    if(3<=len(value)<=5):
        print("Entered characters are ",value)
    else:
        print("Enter strictly 3 to 5 characters")

defaultfun()
defaultfun("hello")