# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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
        return True, select_month()
    elif int(values) == 2:
        print("You chose to add a new birthday...") 
        return True, add_birthday() 
        
    else:
        print("You need to type 1 or 2 to make a choice.")
        return False 
        
    #print(values)    

def select_month(choice = 1):
    """
    Asks the user to choose a month
    asks for an input of a number from 1 to 12
    print an error if a letter is input 
    """
    error = "You must enter a number between 1 and 12"
    print("Which month would you like?")
    print("All months are numbered 1 to 12, so January is 1, February is 2 etc.")
    
    while True:    
        try:
            b_month = int(input("Enter a number to make your selection here:"))
            #b_month = int(b_month)
        except ValueError:
            print(error)
            continue    
        if b_month in range(1,13):
            chosen_month_data(b_month)
            break
        else:
            print(error)


          

def chosen_month_data(values):
    """
    Prints month choice to terminal, and birthday lists
    """
    
    if int(values) == 1:
        print("January Birthdays are\n")
        return True, get_birthday_data()
    elif int(values) == 2:
        print("February") 
        return True, "Feb"
    elif int(values) == 3:
        print("March") 
        return True, "Mar"  
    elif int(values) == 4:
        print("April") 
        return True, "April" 
    elif int(values) == 5:
        print("May") 
        return True, "May"
    elif int(values) == 6:
        print("June") 
        return True, "June"
    elif int(values) == 7:
        print("July") 
        return True, "July"
    elif int(values) == 8:
        print("August") 
        return True, "August"
    elif int(values) == 9:
        print("September") 
        return True, "Sept"
    elif int(values) == 10:
        print("October") 
        return True, "Oct"
    elif int(values) == 11:
        print("November") 
        return True, "Nov" 
    elif int(values) == 12:
        print("December") 
        return True, "Dec"  
    """ 
    not sure if I need this?                                     
    else:
        print("You need to type between 1 and 12 to  choose a month.")
        return False 
    """   

    print(values) 


def get_birthday_data():
    print("checking for birthdays")
    birthday = SHEET.worksheet('Jan')
    birthday_detail = birthday.get_all_values()
    print(birthday_detail)


def main():
    """
    run all program functions
    """
    #first_user_choice() 
    get_birthday_data()
    #select_month() 


print("Welcome to your Birthday Reminder App.\n")     
main()     
