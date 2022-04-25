#snakes and ladders game

import random
import time


#set up variables for players on the board
player1pos = 0
player2pos = 0

print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("                  Welcome to...")
time.sleep(2)
print("               SNAKES AND LADDERS!!")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
time.sleep(2)

#ask for players name
player1 = input("Enter your name player 1: ")
player2 = input("Enter your name player 2: ")
print()
time.sleep(1)
print("Hello," ,player1, "and" ,player2, "")
time.sleep(1)
print()
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("                  LET'S START")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print()

#player 1 roles dice
while True:
    print("Press: ENTER, to roll dice")
    input()
    print(player1, "it's your turn to roll the dice!")
    p1dice = random.randrange(1,12)
    player1pos = player1pos + p1dice
    print(player1, "you got", p1dice)
    print(player1, "your position is", player1pos)