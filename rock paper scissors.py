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

                #rock
                if computer == 'rock':
                    print("It's a draw! No one wins")
                    uS = uS + 1
                    cS = cS + 1

                if computer == 'paper':
                    print("Paper beats rock! You win")
                    uS = uS + 1

                if computer == 'scissors':
                    print("Rock beats scissors! Computer wins")
                    cS = cS + 1

            #paper
            if userplay == 'paper':
                rnd = rnd + 1

                if computer == 'rock':
                    print("Paper beats rock! You win")
                    uS = uS +1

                if computer == 'paper':
                    print("Its a draw! No one wins")
                    uS = uS + 1
                    cS = cS + 1

                if computer == 'scissors':
                    print("Scissors beat paper! Computer wins")
                    cS = cS + 1

            #scissors
            if userplay == 'scissors':
                rnd = rnd + 1

                if computer == 'rock':
                    print("Rock beats scissors! Computer wins")
                    cS = cS + 1

                if computer == 'paper':
                    print("Scissors beat paper! You win")
                    uS = uS + 1

                if computer == 'scissors':
                    print("It's a draw! No one wins")
                    uS = uS + 1
                    cS = cS + 1

            #end of round
            if rnd == 5:
                print("You have reached 5 rounds!")
                time.sleep(1)
                print("Your score was: ",uS,"and the computer score")
                time.sleep(1)
                print("was: ",cS,"meaning...")
                time.sleep(2)

                #winner
                if uS > cS:
                    print("You Won!! well done :]")

                if uS < cS:
                    print("You lost. Oh well :]")

                if uS == cS:
                    print("It's a draw! :]")

    breakpoint() 