import random
number = random.randint(1, 10)

#set count variable to 0
count = 0
import time

while True:
    count = count + 1

    #ask for their number
    print("..............................................")
    userguess = int(input("Enter your guess here: "))
    print("..............................................")
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
        print("You have guessed correct")
        
        #every time you went through the cyle it added 1 to 'count'
        print("You've had", count, "attempts.")
        print()
        time.sleep(1)
        print("Goodbye!")
        break

    #if they have too many guesse the cycle breaks
    elif count == 5:
        print("You have ran out of guesses :[")
        print()
        time.sleep(1)
        print("Goodbye!")
        break
