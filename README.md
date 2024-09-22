# Birthday Reminder App

The Birthday reminder app runs in the Code Institute mock terminal on Heroku.

The app allows the user to access a birthday spreadsheet they have set up in their Google account. They can use the app to check for birthdays that are due in a specific selected month, and also to update the spreadsheet by adding birthdays to a selected month.

## How to use the app

The User is welcomed to the App.<br>
They are asked to select a month by entering a number from 1 to 12, each number corresponds to a month.<br>
If they enter a letter, a number greater than 12 or nothing they are prompted to try again.<br>
Their chosen month is confirmed and the birthdays from their google sheet for that month are displayed as a date and a name.<br>
They are asked if they would like to add a birthday to the currently selected month.<br>
The user is prompted to enter a date and a name, separated by a comma, eg: 21st, Garry.<br>
If they don't follow this pattern, (two strings separated by a comma) they are asked to try again.<br>
If they input correctly the spreadsheet for their chosen month is updated and this is confirmed to them.<br>
They are asked if they would like to restart and check another month or exit, if they want to restart they are taken back to choosing a month, or if they want to exit the app finishes with a 'Goodbye'.

## Credits/Reference

I set up the workarea and connected the Google sheets by following the API demo from the Love Sandwiches walkthrough project. I also consistently checked in with this project as a reminder of how to keep testing along the way and organise the python code.

Referred to [this article](https://www.knowledgehut.com/blog/programming/user-input-in-python) on user input. <br>
Referred to [this article](https://www.toolsqa.com/python/python-while-loop/) for checking the 'while' loop.<br>
Referred to [this article](https://stackoverflow.com/questions/20652527/python-try-except-with-of-if-else) on combination of with, of, if, else usage.<br>
Referred to [this article](https://www.geeksforgeeks.org/how-to-use-a-variable-from-another-function-in-python/) for advice on global variables.<br>
Code for restarting or exiting the game copied from [here](9https://gist.github.com/ArielAleksandrus/9dd5da003162e7f177c3).<br>
Mentor guidance on organization of functions and how to simplify with range selectors and using while True statements to loop if errors are in the input.<br>
Mentor guidance on simplifying flow structure of app when referring to initial flowcharts, comparing functions, seeing what is repeated etc.<br>
