# Import the necessary modules
import random  # Module for generating random numbers
import os  # Module for interacting with the operating system
import time  # Module for dealing with time-related functions
from termcolor import colored  # Import a specific function from the termcolor module
import platform  # Import the 'platform' module to identify the operating system

# Display a message for character creation
print("***Character builder***\n")


# Define a function to roll a dice with a specified number of sides
def roll_dice(sides):
    result = random.randint(1, sides)  # Generate a random number between 1 and the specified number of sides
    return result


# Define a function to calculate character health based on dice rolls
def character_health():
    six_sided = roll_dice(6)  # Roll a six-sided dice
    twelve_sided = roll_dice(12)  # Roll a twelve-sided dice
    result = (six_sided * twelve_sided) / 2 + 10  # Calculate health based on dice rolls
    return result


# Define a function to calculate character stats based on dice rolls
def character_stats():
    six_sided = roll_dice(6)  # Roll a six-sided dice
    twelve_sided = roll_dice(12)  # Roll a twelve-sided dice
    result = (six_sided * twelve_sided) / 2 + 12  # Calculate stats based on dice rolls
    return result


# Display a message for the start of the battle
print("*** Battle time! ***\n")

# Prompt the user to input character details for player one
player_one_name = input(colored("Name your legend: \n", "cyan"))
player_one_char = input(colored("Character type: Human, Elf, Wizzard, Orc: \n", "yellow"))
player_one_health = character_health()  # Calculate health for player one
player_one_stats = character_stats()  # Calculate stats for player one
print(colored("Health: ", "green"), player_one_health)  # Print health in green
print(colored("Strength: ", "red"), player_one_stats)  # Print stats in red
print()
print()

# Prompt the user to input character details for player two
print("*** Who are they battling? ***\n")
player_two_name = input(colored("Name your legend: \n", "cyan"))
player_two_char = input(colored("Character type: Human, Elf, Wizzard, Orc: \n", "yellow"))
player_two_health = character_health()  # Calculate health for player two
player_two_stats = character_stats()  # Calculate stats for player two
print(colored("Health: ", "green"), player_two_health)  # Print health in green
print(colored("Strength: ", "red"), player_two_stats)  # Print stats in red
print()
print()


# Define a function to clear the terminal screen based on the operating system
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")  # For Windows
    else:
        os.system("clear")  # For Unix-like systems


# Display a message for the start of the battle
print("**** Battle time ****\n")
print("*The battle begins!*\n")

# Initialize round counter and winner variable
rounds = 1
winner = None

# Start an infinite loop for the battle simulation
while True:
    clear_screen()  # Clear the terminal screen
    time.sleep(2)  # Pause for 2 seconds

    # Calculate the difference in stats between players
    difference = abs(player_one_stats - player_two_stats) + 1

    # Roll dice for both players
    player_one_dice = roll_dice(6)
    player_two_dice = roll_dice(6)
    print()

    # Compare dice rolls and determine the winner of the round
    if player_one_dice > player_two_dice:
        player_two_health -= difference  # Decrease player two's health
        if rounds == 1:
            print(player_one_name, "wins the first blow")
        else:
            print(player_one_name, "wins round", rounds)
    elif player_two_dice > player_one_dice:
        player_one_health -= difference  # Decrease player one's health
        if rounds == 1:
            print(player_two_name, "wins the first blow")
        else:
            print(player_two_name, "wins round", rounds)
    else:
        print("Their swords clash and they draw in round:", rounds, ".")

    print()
    print(player_one_name, "\n")
    print("Health:", player_one_health)
    print()
    print(player_two_name, "\n")
    print("Health:", player_two_health)
    print()

    # Check if a player's health has dropped to zero or below
    if player_one_health <= 0:
        print(player_one_name, "has died!")
        winner = player_two_name
        break
    elif player_two_health <= 0:
        print(player_two_name, "has died!")
        winner = player_one_name
        break
    else:
        print("They both survived another round!")

    rounds += 1  # Increment the round counter

time.sleep(2)  # Pause for 2 seconds
clear_screen()  # Clear the terminal screen

# Display the winner of the battle
print(winner, "has won in", rounds, "round(s).")
