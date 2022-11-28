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

# ---------------------------- VARIABLES ETC, THE BASE FOR GAME ----------------------------
"""
This part of the code is inspired from
https://www.youtube.com/watch?v=tF1WRCrd_HQ
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


# ---------------------------- INTRO ----------------------------
def get_player_name():
    """
    Creating an input, asking player for their name.
    Validates input if it violates certan criterias,
    if it does then throw an error message and go back to the top.
    A little help from my mentor to get it started.
    """
    while True:
        name = input("Hello, please enter your name:\n").strip().lower()
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


# ---------------------------- SELECT RULES OR PLAY GAME ---------------------
def rules_option():
    """
    Creating an input giving user 2 options to display rules or play game with
    a yes or no answer.
    Validates input if it violates certan criterias, answer must be
    'yes' or 'no'.
    if it does, throw an error message and go back to the top.
    Some basic styling to 'print' to make it easier for user to read the
    terminal.
    """
    while True:
        rules = input("Would you like to display the rules? please enter 'yes' or 'no'\n").strip().lower()
        # Rules will display if player enter "yes".
        if rules == 'yes':
            print("------------------------------------------------------")
            print("")
            print("Rules:\n1. Contains a 5x5 grid with 5 ships randomly placed in the grid.\n2. Player will have 10 bullets to hit the ships.\n3. Player would choose a row & a column (1-5 & A-E) to aim their shot.\n4. Every missed or hit ship will show in the grid.\n5. Player wins if they shot all ships down before running out of bullets, or else you will lose.")
            print("")
            print("Game Symbols:\n' ' = Empty space\n- = Missed shot\nX = Ship's been shot.")
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

        else:
            print("Please enter 'yes' or 'no'\n")
            continue
        break


# ---------------------------- SELECT RULES OR PLAY GAME ---------------------

"""
This part of the code is inspired from
https://www.youtube.com/watch?v=tF1WRCrd_HQ
"""

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


# ---------------------------- SHIPS ON GRID ----------------------------
def ships_from_comp(grid):
    """
    Creating a function that will let the computer randomly place 5 ships
    on the grid.
    Using a for loop so computer will place 5 ships on the grid,
    between the numbers 0,4 (1-5 on grid).
    """
    for ship in range(5):
        ship_row, ship_column = randint(0,4), randint(0,4)
        while grid[ship_row][ship_column] == "X":
            ship_row, ship_column = get_player_shots()
        grid[ship_row][ship_column] = "X"


# ---------------------------- PLAYERS INPUT ----------------------------
def get_player_shots():
    """
    Creating a function with an input to get user to choose where they want to
    aim their shot.
    I created 2 while statments explaining how to enter correct input,
    and throw an error if it's not valid.
    Returning whole numbers and letters to numbers.
    A little help from code institute's tutor (jason) to get it going properly.
    """
    column = input("Enter a column(A-E) to aim your shot:\n").strip().upper()
    # Error message if player doesn't write correct input for columns
    while column not in "ABCDE":
        print("------------------------------------------------------")
        print("")
        print("Please enter A, B, C, D or E)")
        print("")
        print("------------------------------------------------------")
        column = input("Enter a column to aim your shot:\n").strip().upper()

    row = input("Enter a row(1-5) to aim your shot:\n").strip()
    # Error message if player doesn't write correct input for rows
    while row not in "12345":
        print("------------------------------------------------------")
        print("")
        print("Please enter 1, 2, 3, 4 or 5\n")
        print("")
        print("------------------------------------------------------")
        row = input("Enter a row(1-5) to aim your shot:\n").strip()
    return int(row) - 1, letters_to_num[column]


# ---------------------------- ROUNDS & HITS/MISSED SHOTS --------------------
def count_shots(grid):
    """
    Creating a function that will keep the count for how many ships that got
    shot down.
    Using a loop and if statement to increment score when row/column hits X.
    When all ships been shot down it end game,
    (creating another function below to end it when this one hits 5.).
    """
    count = 0
    for row in grid:
        for column in row:
            if column == "X":
                count += 1
    return count


def run_game():
    # Max score of how many shots players can use before game ends.
    total_shots = 10

    # Starting with no shots shot
    # before player enters their first shot.
    while total_shots > 0:
        display_grid(GUESS_GRID)
        row, column = get_player_shots()

        # If player guess the same row/column again this print will show
        if GUESS_GRID[row][column] == "O":
            print("------------------------------------------------------")
            print("")
            print("You already tried to aim here")
            print("")
            print("------------------------------------------------------")

        # If player hits a ship, X will show on the grid
        # When player hits a ship it will count the score down of total shots
        elif HIDDEN_GRID[row][column] == "X":
            print("------------------------------------------------------")
            print("")
            print("You shot down a ship, good job soldier!")
            print("")
            print("------------------------------------------------------")
            GUESS_GRID[row][column] = "X"
            total_shots -= 1

        # If player missed a ship, O will show in the grid
        # When player miss a ship it will count the score down of total shots
        else:
            print("------------------------------------------------------")
            print("")
            print("You failed to shoot down a ship, don't give up!")
            print("")
            print("------------------------------------------------------")
            GUESS_GRID[row][column] = "O"
            total_shots -= 1

        # Here we stop the game once Player shoots down all ships
        if count_shots(GUESS_GRID) == 5:
            print("------------------------------------------------------")
            print("")
            print("Wihoo, you succeded the mission and won!")
            print("")
            print("------------------------------------------------------")
            break

        # When player runs out of shots, game will end.
        if total_shots == 0:
            print("------------------------------------------------------")
            print("")
            print("Oh no, you failed the mission and lost!")
            print("")
            print("------------------------------------------------------")

# ---------------------------- MAIN FUNCTION ----------------------------
def main():
    """
    Run all functions data
    """
    player_name = get_player_name()
    print("------------------------------------------------------")
    print("")
    print(f"Alright {player_name}, let's get started!\n")
    print("")
    print("------------------------------------------------------")

    rules_option()

    ships_from_comp(HIDDEN_GRID)

    run_game()

    display_grid(HIDDEN_GRID)

    print("\nSolution vivible above\n")
    print(f"\nThank you for playing, see you next time {player_name}")


main()