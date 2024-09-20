# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json') 
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('birthday_spreadsheet') 


def first_user_choice():
    """
    Welcome user and ask them to choose
    1- check for birthdays
    2- add a new birthday to the spreadsheet
    """

    print("Welcome to your Birthday Reminder App.")
    print("Please enter")
    print("1 to check for birthdays, or")
    print("2 to add a birthday to the spreadsheet.\n")

    choice = input("Enter '1' or '2' to make your selection here:")
    choice = int(choice)
    if choice == 1:
        print("You chose to check for birthdays.")
    elif choice == 2:
        print("You chose to add a new birthday")    
    else:
        print("You need to type 1 or 2 to make a choice.")    

    

first_user_choice()    