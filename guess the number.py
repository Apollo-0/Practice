import random
number = random.randint(1, 10)

#set count variable to 0
count = 0
import time

print(".......................................")
print("GUESS THE NUMBER!")
print(".......................................")
print()
time.sleep(2)

while True:
    count = count + 1

    #ask for their number
    print()
    userguess = int(input("Enter your guess here: "))
    print()

    #if their number is too high and tell them
    if userguess > number:
        time.sleep(1)
        print("Nope, that's too high!")

    #if their number is too low and tell them
    if userguess < number:
        time.sleep(1)
        print("Nope, that's too low!")

    #if the number is tha same say so, and break cycle
    if userguess == number:
        time.sleep(1)
        print("You have guessed correct")
        
        #every time you went through the cyle it added 1 to 'count'
        print("..................................................................")
        time.sleep(1)
        print("You've had", count, "attempts.")
        print()
        time.sleep(1)
        print("Goodbye!")
        print("..................................................................")
        break

    #if they have too many guesses the cycle breaks
    elif count == 5:
        print("You have ran out of guesses :[")
        print()
        time.sleep(1)
        print("Goodbye!")
        break
