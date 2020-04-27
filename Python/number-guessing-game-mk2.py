#Project Revise
#Now featuring fewer lines of code and def functions and new ways
#to substitue values with '.format'

import random

while True:
        playerName = input("Enter your name>")
        try:
            int(playerName)
            playerNameType = "int"
        except ValueError:
            try:
                float(playerName)
                playerNameType = "float"
            except ValueError:
                playerNameType = "string"
        if playerNameType != "string":
            print("Please try again")
            continue
        else:
            print("Hi, "+str(playerName)+"!")
            break

def numberGuessGame():
    guesses = 0         #b for baby                           x for extreme
    difficultyRanges = {'b': 10, 'e': 20, 'm': 50, 'h': 100, 'x': 1000}

    while True:
        difficulty = input("Type 'b' for a 10 digit range, 'e' for 20, 'm' for 50, 'h' for 100, 'x' for 1,000:").lower()
        try:
            number = random.randint(0, difficultyRanges[difficulty])
            print("Guess a number from 0 to {}".format(difficultyRanges[difficulty]))
            break
        except ValueError:
            print("Please put in a number")

    while True:
        try:
            guess = int(input("Your guess: "))
            guesses += 1
            if number == guess:
                print("Correct guess! You used {} guesses.".format(guesses))
                return numberGuessGame() if input("Play again? Press 'y' to play again or any key to exit.").lower() == 'y' else 0
            elif guess < 0 or guess > difficultyRanges[difficulty]:
                print("Your guess was out of range!")
            else:
                if number < guess:
                    print("Too High, guess again")
                else:
                     print("Too Low, guess again")
        except ValueError:
            print("Must be an integer value")

def main():
    numberGuessGame()
if playerNameType == "string":
    main()
