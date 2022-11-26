import gspread
from google.oauth2.service_account import credentials

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

player_name = get_player_name()
print(f"Alright {player_name}, let's get started!\n")