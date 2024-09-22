# Birthday Reminder App

The Birthday reminder app runs in the Code Institute mock terminal on Heroku.

The app allows the user to access a birthday spreadsheet they have set up in their Google account. They can use the app to check for birthdays that are due in a specific selected month, and also to update the spreadsheet by adding birthdays to a selected month.

[Here is the app](https://birthday-reminder-620bb10397e2.herokuapp.com/)

[Here is the spreadsheet](https://docs.google.com/spreadsheets/d/1B1Lq1--t_gRSvk8bO3cHkOmlPVF0pA2te1agPnkIjew/edit?usp=sharing)


![Screenshot of the Birthday Reminder App](/assets/birthdayappscreen.png)


## How to use the app

The User is welcomed to the App.<br>
They are asked to select a month by entering a number from 1 to 12, each number corresponds to a month.<br>
If they enter a letter, a number greater than 12 or nothing they are prompted to try again.<br>
Their chosen month is confirmed and the birthdays from their google sheet for that month are displayed as dates and a name in a list.<br>
They are asked if they would like to add a birthday to the currently selected month.<br>
The user is prompted to enter a date and a name, separated by a comma, eg: 21st, Garry.<br>
If they don't follow this pattern, (two strings separated by a comma) they are asked to try again.<br>
If they input correctly the spreadsheet for their chosen month is updated and this is confirmed to them.<br>
They are asked if they would like to restart and check another month or exit, if they want to restart they are taken back to choosing a month, or if they want to exit the app finishes with a 'Goodbye'.

## Features
### Existing Features
The user is presented with an input to select a month.
The user can call data from the google spreadsheet of their lists of birthdays from the selected month.
The user can add birthdays to their selected month and update the google sheet.
- Input Validation and error checking
    - You can only enter a number between 1 and 12 to choose a month.
    - You can only enter two strings separated by a comma for the date and name input for a new birthday to be added.
    - The user can exit the app or choose another month to access.    
### Future features
- Allow the user to exit the app after they have selected the month and checked for birthdays, currently they are asked if they would like to add a birthday but have no option to leave if they do not want to.
- Improve the presentation of the data pulled from the google sheet when you check what birthdays there are, I would like to take away all the brackets, so it reads more cleanly as a list of dates with names.
- Improve the validation checks for the input for the new birthday date and name. Currently it just checks the input is two strings, I would like the first string to be confirmed as a date number that could only occur in the already selected month. And the second string to be confirmed as a name that does not exceed a certain length of characters.
- I would like to understand how the google sheets relationship could work further, so rather than updating and calling from a spreadsheet, to engage with a google calendar.

## Testing
I have manually tested the following;
- Passed the code through Pep8, there were warnings for white space, and various input statements and print statements that were too long for the app terminal window, I adjusted these accordingly, then Code passed validation
- Tested inputs, so where a number is required for the month, I tested what would happen if a larger number was input, a letter or nothing at all.
- Tested the input of two strings, so tried inputing nothing, and more than one string.
- Tested in my local terminal and the Code Institute Heroku Terminal.

## Bugs
I had issues with choosing how to add inputs for adding a birthday.
I tried separating out the inputs so you would first input a number, and then input a name. I wanted to do this in order to validate each input separately, yet I struggled to 'bring them back together' and then pass onto the google sheet. I decided to simplify it down to one input, but would like to solve this as a future feature as I think it would be more accurate for the inputs to be validated individually.


## Credits/Reference

I set up the work area and connected the Google sheets by following the API demo from the Love Sandwiches walkthrough project. I also consistently checked in with this project as a reminder of how to keep testing along the way and organise the python code. I referred to the Readme example for the project 3 submission guidelines.

Referred to [this article](https://www.knowledgehut.com/blog/programming/user-input-in-python) on user input. <br>
Referred to [this article](https://www.toolsqa.com/python/python-while-loop/) for checking the 'while' loop.<br>
Referred to [this article](https://stackoverflow.com/questions/20652527/python-try-except-with-of-if-else) on combination of with, of, if, else usage.<br>
Referred to [this article](https://www.geeksforgeeks.org/how-to-use-a-variable-from-another-function-in-python/) for advice on global variables.<br>
Code for restarting and exiting the game copied from [here](https://gist.github.com/ArielAleksandrus/9dd5da003162e7f177c3).<br>
Mentor guidance on organization of functions and how to simplify with range selectors and using while True statements to loop if errors are in the input.<br>
Mentor guidance on simplifying flow structure of app when referring to initial flowcharts, comparing functions, seeing what is repeated etc.<br>

## Deployment
This project was deployed using Code Institute's mock terminal for Heroku.
The live project is [here](https://birthday-reminder-620bb10397e2.herokuapp.com/)

- Steps for deployment
    - Fork or clone this repository
    - Create a new Heroku app
    - Set the buildbacks to Python and NodeJS in that order
    - Link the Heroku app to the repository
    - Click on Deploy
