#Rock paper scissors game

#all the scores and imports
import sys
import random
import time
rnd = 0
score = 0
uS = 0
cS = 0

print("....................................")
print("!!ROCK PAPER SCISSORS SHOOT!!")
print("....................................")
print()
time.sleep(2)

#the computer and users choices
choices = ['rock', 'paper', 'scissors']

print("RULES")
print("The only rule is to type in all lowercase")
time.sleep(1)
print("Also make sure your spellings are correct!")
time.sleep(2)
print("Have fun! :]")
print()
print(".................................................")
print()
time.sleep(2)

while True:

    print("""
    PRESS
    1) TO CONTINUE TO GAME
    2) TO QUIT GAME/LEAVE""")
    print()

    menu_choice = input("Enter your choice here: ")

    if menu_choice == '1':
        while True:
            computer = random.choice(choices)

            print()
            print("Enter your choice: rock / paper / scissors")
            print()
            userplay = input()
            time.sleep(1)

            if userplay == 'rock':
                rnd = rnd + 1

                if computer == 'rock':
                    print("It's a draw! No one wins")
                    uS = uS + 1
                    cS = cS + 1