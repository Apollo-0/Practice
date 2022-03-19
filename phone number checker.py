#Phone Number Checker

import time
numbers = "0123456789"

#set flag to be True
valid = True

##print a welcome messages
print(".......................................................")
print("Welcome to phone number checker!")
print(".......................................................")
print()

#start a while loop
while True:

    print("Please enter your phone number here: ")
    phonenumber = input()

    #first number should be a 0
    if phonenumber[0] != "0":
        valid = Falseprint("Your first number doesn't start with 0")
        time.sleep(1)
        print("Please try again")
        print()

    #second number should be 7
    if phonenumber[1] != "7":
        valid = Falseprint("Your second number isn't a 7")
        time.sleep(1)
        print("Please try again")
        print()
        