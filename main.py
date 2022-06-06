#This is a game loop
import random
import time

print(
    "\tWelcome to our guessing game.\n\nI have a number in my mind between 1 and 100. You have 5 guesses to tell me what the number is.\nUnleash your Psyche :)\n\n "
)
time.sleep(1)
guess = int(input("What is your guess? \n"))
correctNumber = random.randint(0, 100)
guessCount = 1

while guess != correctNumber and guessCount < 5:
    time.sleep(1)
    if guess < correctNumber:
        guess = int(input("Incorrect guess. \nTry something higher: "))
    else:
        guess = int(input("Incorrect guess. \nTry something lower: "))
    guessCount += 1  #Tally number of guesses

if guess == correctNumber:
    time.sleep(1)
    print(
        f"\nYay!!! You guessed right.\nThe correct number is {correctNumber}.\nIt took you {guessCount} guesses :)"
    )
else:
    print(
        f"\nSnap!!! You need to work on your psyche :(\nThe correct number is {correctNumber}.\n"
    )
  
