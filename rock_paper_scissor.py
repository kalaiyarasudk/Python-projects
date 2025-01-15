
from random import choice
import sys
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    Scissor = 3


game = "Rock paper scissors".upper() 
print(game.center(45,"-"))
print("")
playerChoice = int(input("Enter your choice\n1.Rock\n2.Paper\n3.Scissors\n"))
if playerChoice < 1 or playerChoice > 3:
    sys.exit("Please enter only 1,2 and 3")

print("")
computerChoice = int(choice("123"))
print("You choose ".ljust(20,'-'), str(RPS(playerChoice)).replace("RPS.",""))
print("Computer choose ".ljust(20,'-'), str(RPS(computerChoice)).replace("RPS.",""))
print("")

if playerChoice == 1 and computerChoice == 3:
    print("Player win!")
elif playerChoice == 2 and computerChoice == 1:
    print("Player Win!")
elif playerChoice == 3 and computerChoice == 2:
    print("player win!")
elif playerChoice == computerChoice:
    print("Tie game!")
else:
    print("Computer Win!")
