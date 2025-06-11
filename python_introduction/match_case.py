#Import the random module: At the beginning of your code, add the line import random. 
# This allows you to use functions from the random module, like generating random numbers.
import random

#Generate a secret number:you can adjust the range if you want
random.randint(1, 10)

#Store this in a variable called secret_number.
secret_number = random.randint(1, 10)
#This gives you a different number between 1 and 10 every time the game runs.

#Get user’s guess: Prompt the user to guess the number using input(). 
# Convert the user’s input to an integer using int(). Store this in a variable called guess.
guess = int(input("Guess a number between 1 and 10: "))

#Match the guess
result = "correct" if guess == secret_number else "low" if guess < secret_number else "high"

match result:
    case "correct":
        print("🎉 Congratulations, you guessed it!")
    case "low":
        print("📉 Nope, your guess is a bit low. Give it another shot!")
    case "high":
        print("📈 Oops, your guess is a bit high. Try again!")

#Offer to play again: Ask the user if they want to play again using an if statement and user input.
play_again = input("Do you want to play again? (yes/no): ").lower()
if play_again == "yes":
# repeat the whole game logic (best done in a while loop)
 while True:
    # game logic here
    
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
