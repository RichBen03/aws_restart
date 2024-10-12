#this imports the module random which contains reusable code and functions
import random 

#using the print function to set the instructions to the game
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

#using the module's function randIntto generate a random number and storeit in a variable
number = random.randint(1,10)

#intializes a checker 
isGuessRight = False

#executes a while loop code as long as the guess is not correct
while isGuessRight != True:
    guess=input("Guess a number between 1 and 10. ")
    
    #compares the input of the user and the random generated number
    if int(guess)== number:
        print("you guessed {}. That is correct! You win".format(guess))
        
        #checks if the guess is True
        isGuessRight=True
    else:
        print("You guessed {}. Sorry that isn't it. Try again.".format(guess))