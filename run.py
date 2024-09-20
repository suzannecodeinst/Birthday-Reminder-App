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
    print choice to terminal and alert if not correct input made.
    """

    print("Welcome to your Birthday Reminder App.")
    print("Please enter")
    print("1 to check for birthdays, or")
    print("2 to add a birthday to the spreadsheet.\n")


    while True:
        choice = input("Enter '1' or '2' to make your selection here:")
        choice = int(choice)
    
        if validate_data(choice):
            #print("works")
            break

def validate_data(values):
    """
    Checks user choice input is either 1 or 2.
    Raises an error if not correct input.
    """
    if int(values) == 1:
        print("Ok, let's check for birthdays...")
        return True
    elif int(values) == 2:
        print("You chose to add a new birthday...") 
        return True
    else:
        print("You need to type 1 or 2 to make a choice.")
        return False 
        
    print(values)    

def select_month(choice = 1):
    """
    Asks the user to choose a month
    asks for an input of a number from 1 to 12
    """
    while True:
        print("Which month would you like?")
        print("All months are numbered 1 to 12, so January is 1, February is 2 etc.")
        b_month = input("Enter a number to make your selection here:")
        b_month = int(b_month)

        if validate_month_data(b_month):
            print("you chose month..")
            break


          

def validate_month_data(values):
    """
    Checks user choice input for a month is between 1 and 12 inclusive.
    Raises an error if not correct input.
    """
    if int(values) == 1:
        print("January")
        return True
    elif int(values) == 2:
        print("February") 
        return True
    elif int(values) == 3:
        print("March") 
        return True  
    elif int(values) == 4:
        print("April") 
        return True 
    elif int(values) == 5:
        print("May") 
        return True
    elif int(values) == 6:
        print("June") 
        return True
    elif int(values) == 7:
        print("July") 
        return True
    elif int(values) == 8:
        print("August") 
        return True
    elif int(values) == 9:
        print("September") 
        return True
    elif int(values) == 10:
        print("October") 
        return True
    elif int(values) == 11:
        print("November") 
        return True 
    elif int(values) == 12:
        print("December") 
        return True                                    
    else:
        print("You need to type between 1 and 12 to make choose a month.")
        return False 
        
    print(values)      
   
       

first_user_choice() 
select_month()  
