# BATTLESHIP
IMAGE HERE

### Play the game here!


## Description

How to play:
1. Battleship contains a 5x5 grid with 5 hidden ships randomly placed in the grid.
2. Player will have 10 bullets to hit the ships.
3. Player must choose a row & a column (1-5 & A-E) to aim their shot.
4. Every missed or hit ship will show in the grid.
5. Player wins if they shoot all 5 ships down before running out of bullets,
   or else they will lose.

Game Symbols:
" " = Empty space
O   = Missed shot
X   = Ship's been shot.


## Index - Table of contents

* [Description](#description)
* [Index - Table of contents](#index-table-of-contents)
* [User Experience](#user-experience)
* [Structure](structure)
* [Features](#excisting-features)
* [Design](#design)
* [Technologies used](#technological-used)
* [Tests](#testing)
* [Deployment](#deployment)
* [Credits](#credits)


## User Experience
A.First Time Visitor Goals
a. As a first time visitor, I want to quick and easily understand the game's purpose.
b. As a first time visitor, I want the website to be readable and clear to follow the instructions.

B.Returning Visitor Goals
a. As a returning visitor, I want to easily navigate through the rules to find out how this game works.


## Structure


## Excisting Features

f1 Intro,
   Created an input to welcome user and ask them kindly to enter their name.
   I used strip() & lower() to remove any extra spacing in the start or -& at the end of the input.

f2 Options,
   Created an input to display 2 options, either play the game or to display the rules.
   User will enter "yes" or "no".
   With a little reminder from my mentor Brian I used strip() & lower() to remove any extra spacing in the start or -& at the end of the input.


## Design

* Intro, options:
  Using multible print statements to make the site more readable.
  I used prints to print out a line over and under the messages I wanted user to read and added some prints to print an empty line, this would cause some space where the message pops up.


## Technological used

Language used,
  Python 3.8.11


## Tools


## Testing
Problems i got
https://www.interviewqs.com/ddi-code-snippets/break-long-line-python

## Deployment

The site was created in GitHub pages, these are the steps to deploy:
Log in to GitHub and go to repositories.
In GitHub on the right side of the repository click on settings.
In settings on the left side menu select "Pages".
Under branch, select "Main" and select folder "(Root)"
Press save and the page will automatically refresh and your site will be att the top. It might take a few minutes, be patient.


## Credits

Used template from code institute's Walk through project ["Love-Sandwiches"](https://github.com/Code-Institute-Org/python-essentials-template)

Game structure comes from this [video](https://www.youtube.com/watch?v=tF1WRCrd_HQ)

Used as an inspiration for making rules appear for user: [Iama3191](https://github.com/iama3191/hangman)