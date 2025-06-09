# Define a function which accepts a character and return toggle of it.

def chartoggle(ch):
    if(ch.isalpha()and len(ch)==1):
        print(ch.swapcase())
ch=input("Enter a character")
chartoggle(ch)