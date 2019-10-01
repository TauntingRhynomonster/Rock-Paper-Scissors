# Ryan
# Rock Paper Scissors
# rps.py
import random
# Variables
pScore = 0
cScore = 0
ties = 0
cMoves = ["rock", "paper", "scissors"]
# Wolcome Message
# Print a welcome message
print("Welcome to Rock Paper Scissors")
# Prompt for name
pName = input("What is your name? ")


# Score Tracker
# Make a function
def printScore():

	# Prints score:
	print("Score: ")
# Shows player score
	print(pName + ": " + str(pScore))
# Shows computer score
	print("Computer Score: " + str(cScore))
# Shows how many ties
	print("Ties: " + str(ties))

# Game Loop
# loop until q is entered
while True:
	# prompt for player move (r, p, s, q)
	pMove = input("Enter 'r' for Rock, 'p' for Paper, 's' for Scissors or 'q' for Quit")
# print the score
	printScore()
# check if q is entered if so end the game
	elif pMove = "q":
		break
# get a computer move (random)
	cMove = random.choice(cMoves)

# compare player move with the computer move
# player pick rock
	elif pMove == "r":
		print(pName + " picked rock")
		if cMove == "rock":
			print("Computer picks Rock")
			print("Tie")
			ties += 1
		elif cMove == "paper":
			print("Computer picks Paper")
			print("Paper covers Rock")
			cScore += 1
		else: 
			print("Computer picks scissors")
			print("Rock breaks scissors")
			pScore += 1
# player pick paper
	elif pMove == "p":
		pass
# player pick scissors
	elif pMove == "s":
		pass
# Check if pMove is valid
	else:
		print("That is not an option")