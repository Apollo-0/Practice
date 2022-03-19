#Phone Number Checker

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
        valid 