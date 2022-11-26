import gspread
from google.oauth2.service_account import credentials
from random import randint


# ---------------------------- Battleship ----------------------------
"""
Rules:
1. Contains a 5x5 grid with 5 ships randomly placed in the grid.
2. Player will have 10 bullets to hit the ships.
3. Player would choose a row & a column (1-5 & A-E) to aim their shot.
4. Every missed or hit ship will show in the grid.
5. Player wins if they shot all ships down before running out of bullets,
   or else you will lose.

Game Symbols:
" " = Empty space
- = Missed shot
X = Ship's been shot.

          A   B   C   D   E
grid =  1   |   |   |   |   |
        2   |   |   |   |   |
        3   |   |   |   |   |
        4   |   |   |   |   |
        5   |   |   |   |   |
"""


# ---------------------------- INTRO ----------------------------

def get_player_name():
    """
    Creating an input, asking player for their name.
    Validates input if it violates certan criterias,
    if it does then throw an error message and go back to the top.
    A little help from my mentor to get it started.
    """
    while True:
        name = input("Hello, please enter your name:\n").strip()
        # Name will contain at least 1 character.
        if len(name) < 1:
            print("Please enter name that is at least 1 letter\n")
            continue
        
        # Name will contain only letters.
        if not name.isalpha():
            print("Please enter a name that only contains letters\n")
            continue
        break
    return name


# ---------------------------- SELECT RULES OR PLAY GAME ----------------------------
def rules_option():
    """
    Creating an input, giving user 2 options to display rules or play game with a yes or no answer.
    Validates input if it violates certan criterias. (answer must be 'yes' or 'no'),
    if it does, throw an error message and go back to the top.
    Some basic styling to 'print' to make it easier for user to read in the terminal.
    """
    while True:
        rules = input("Would you like to display the rules? please enter 'yes' or 'no'\n").strip()
        # Rules will display if player enter "yes".
        if rules == 'yes':
            print("------------------------------------------------------")
            print("")
            print("Rules:\n1. Contains a 5x5 grid with 5 ships randomly placed in the grid.\n2. Player will have 10 bullets to hit the ships.\n3. Player would choose a row & a column (1-5 & A-E) to aim their shot.\n4. Every missed or hit ship will show in the grid.\n5. Player wins if they shot all ships down before running out of bullets, or else you will lose.")
            print("")
            print("Game Symbols:\n"  " = Empty space\n- = Missed shot\nX = Ship's been shot.")
            print("")
            print("------------------------------------------------------")
            continue

        # Game will start if player enter "no".
        if rules == 'no':
            print("------------------------------------------------------")
            print("")
            print("Game starts now..")
            print("")
            print("------------------------------------------------------")
            # Calling function to display when player say no. (come back to fix this)
            display_grid(HIDDEN_GRID)
            continue

        else:
            print("Please enter 'yes' or 'no'\n")
            continue
        break
    return rules


# ---------------------------- BUILDING THE GRID ----------------------------
"""
This part of the code is inspired from https://www.youtube.com/watch?v=tF1WRCrd_HQ
"""
# Grid to set ships placement
HIDDEN_GRID = [[" "] * 5 for x in range(5)]
# Grid to show players shot and missed shots
GUESS_GRID = [[" "] * 5 for i in range(5)]

letters_to_num = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4
}

def display_grid(grid):
    """
    Creating a function to display the grid.
    Converted letters to numbers in code above,
    since this function is using numbers to count and not letters.
    """
    print("  A B C D E")
    row_num = 1
    # Looping through our list row_num.
    for row in grid:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num += 1


# ---------------------------- MAIN FUNCTION ----------------------------

def main():
    """
    Run all functions data
    """
    player_name = get_player_name()
    print(f"Alright {player_name}, let's get started!\n")

    rules_answer = rules_option()

main()