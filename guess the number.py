import random
number = random.rand7int(1, 10)

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

    #see if their number is too highand tell them
    if userguess > number:
        time.sleep(1)
        print("Nope, that's too low!")