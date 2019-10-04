import random

print("=======================")
print("    Guess My Number    ")
print("      By Skyler P      ")
print("=======================")
print("")

name = input("What is your name?")
print("")

print("I'm thinking of a number between 0 and 100. Can you guess it?")
the_number = random.randint(1,99)

guess = -1

while guess != the_number:
    guess_text = input("What is your guess?")
    guess = int(guess_text)

    if guess > 100 or guess < 0:
        print("BRUHHHH pick between 0 and 100.")
    if guess < the_number:
        print(f"Sorry {name}, but your guess is to LOW. Try again.")
    elif guess > the_number:
        print(f"Sorry {name}, but your guess is to HIGH. Try again.")
    elif guess > 100 or guess < 0:
        print("Listen up pal thats not between 0 and 100.")
    else:
        print(f"You guessed it! Congratulations, {name}!")\

print("Thank You For Playing!!!!!")