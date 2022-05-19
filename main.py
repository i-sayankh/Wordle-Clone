import pandas as pd
import csv
import random
import typer
import colorama
from colorama import Fore, Style

# Reading the text file and converting into CSV File
dataframe1 = pd.read_csv("five_letter_words.text", delimiter=",")
dataframe1.to_csv('five_letter_words.csv', index=None)

# Creating a list of all five-letter words from the dataset
with open('five_letter_words.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

# Choosing a random five-letter word
chosen_word = random.choice(data)[0]
# For debugging purpose only
# print(f"The Chosen word is: {chosen_word}")
chosen_word_length = len(chosen_word)
display_text = ""


def wordle():
    # Instructions
    print("Guess the WORDLE in six tries.")
    print("Each guess must be a valid five-letter word. Hit the enter button to submit.")
    print("After each guess, the color of the lettres will change to show how close your guess was to the word.")
    print(Fore.GREEN + "W", end="")
    print(Style.RESET_ALL, end="")
    print("EARLY")
    print("The letter 'W' is in the word and in the correct spot.")
    print("P", end="")
    print(Fore.YELLOW + "I", end="")
    print(Style.RESET_ALL, end="")
    print("LLS")
    print("The letter 'I' is in the word but in the wrong spot.")
    print("VAG", end="")
    print(Fore.RED + "U", end="")
    print(Style.RESET_ALL, end="")
    print("E")
    print("The letter 'U' is not in the word in any spot.\n")

    # Number of attempts = 6
    attempt = 6

    # A flag variable that indicates the game is on.
    is_on = True
    while is_on:

        # Taking user input
        guess = typer.prompt("Guess a five letter word ").lower()

        # Checking for invalid input
        if len(guess) != 5:
            print("Invalid Input!! PLease Enter a five-letter word.")
            guess = typer.prompt("Guess a five letter word ").lower()

        # If the player guesses correctly the game will over and he/she wins.
        if guess == chosen_word:
            print(Fore.GREEN, f"{guess}", end="")
            print(Style.RESET_ALL)
            typer.echo("Congratulations!! You've guessed correctly.")
            is_on = False

        # Attempt decreases by 1 for each guess
        else:
            attempt -= 1

            # Checking the letters of user guess and changing their text color according to the game rules.
            for position in range(chosen_word_length):
                if guess[position] == chosen_word[position]:
                    print(Fore.GREEN + f"{guess[position]}", end="")
                elif guess[position] != chosen_word[position] and guess[position] in chosen_word:
                    print(Fore.YELLOW + f"{guess[position]}", end="")
                elif guess[position] != chosen_word[position] and guess[position] not in chosen_word:
                    print(Fore.RED + f"{guess[position]}", end="")
                global display_text
                display_text += guess[position]

            # Reset to default color
            print(Style.RESET_ALL)
            if display_text == chosen_word:
                typer.echo("You've guessed correctly.")
                is_on = False
            else:
                # If the player run out of guesses the game will over.
                if attempt < 1:
                    print("You've run out of attempts!!")
                    print(f"The Correct Answer is: {chosen_word}.")
                    is_on = False
                    break
                typer.echo(f"Incorrect Guess! You've {attempt} attempts remaining.")


if __name__ == "__main__":
    typer.run(wordle)
