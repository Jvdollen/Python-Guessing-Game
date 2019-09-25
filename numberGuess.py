gameOver=False
import random
theComputerNumber = random.randint(1,1000000)
numberOfGuesses=0
lowGuessRange=1
highGuessRange=1000000
while not gameOver:
    print("Enter a guess in range from ", lowGuessRange, "to ",highGuessRange)
    playerGuess = int (input("Enter your guess: "))
    if(numberOfGuesses == 20):
        print("You've run out of guesses.")
        gameOver=True
    if(theComputerNumber==playerGuess):
        print("You've guessed the number.")
        gameOver = True
    if(playerGuess<lowGuessRange or playerGuess > highGuessRange):
        print("Guess out of range, try again")
        continue
    if(playerGuess< theComputerNumber):
        numberOfGuesses+=1
        lowGuessRange = playerGuess
        continue
    if(playerGuess > theComputerNumber):
        numberOfGuesses+=1
        highGuessRange = playerGuess
        continue

            
