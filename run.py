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

   

def select_month():
    """
    Asks the user to choose a month
    asks for an input of a number from 1 to 12
    print an error if a letter is input 
    """
    error = "You must enter a number between 1 and 12"
    print("Choose a month to get started")
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
    Selects chosen month worksheet from the Google Doc
    and returns the correct sheet as a global variable to pass to 
    the next function
    prints the chosen month to terminal
    """
    global month_result
    if int(values) == 1:
        print("January")
        month_result = 'Jan'
        return True
    elif int(values) == 2:
        print("February")
        month_result = 'Feb' 
        return True
    elif int(values) == 3:
        print("March")
        month_result = 'March' 
        return True  
    elif int(values) == 4:
        print("April")
        month_result = 'April'  
        return True 
    elif int(values) == 5:
        print("May")
        month_result = 'May'  
        return True
    elif int(values) == 6:
        print("June")
        month_result = 'June'  
        return True
    elif int(values) == 7:
        print("July")
        month_result = 'July'  
        return True
    elif int(values) == 8:
        print("August")
        month_result = 'Aug'  
        return True
    elif int(values) == 9:
        print("September")
        month_result = 'Sept'  
        return True
    elif int(values) == 10:
        print("October")
        month_result = 'Oct'  
        return True
    elif int(values) == 11:
        print("November")
        month_result = 'Nov'  
        return True 
    elif int(values) == 12:
        print("December")
        month_result = 'Dec'  
        return True  
    """ 
    not sure if I need this? does the above last elif need to be else?                                     
    else:
        print("You need to type between 1 and 12 to  choose a month.")
        return False 
    """   

def first_user_choice():
    """
    Ask them to choose
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
        print(f"Ok, let's check for birthdays in {month_result}...")
        return True, get_birthday_data()
    elif int(values) == 2:
        print(f"You chose to add a new birthday to {month_result}") 
        return True, add_birthday() 
        
    else:
        print("You need to type 1 or 2 to make a choice.")
        return False 
        
    #print(values) 



def get_birthday_data():
    """
    gets the previously selected month from the worksheet and prints the
    data to the terminal.
    need to print the data nicer...
    """
    global month_result
    birthday = SHEET.worksheet(month_result)
    birthday_detail = birthday.get_all_values()
    print(birthday_detail)


def add_birthday(choice = 2):
    """
    Asks user for new birthday data
    enter a date and a name, validates data
    if ok, progress to function to update google sheet
    """

    while True:
        print("Please enter the date of the birthday you would like to add, followed by the name.")
        print("Data should be one date and a name, separated a comma.")
        print("Example: 21st, Garry\n")

        birthday_str = input("Enter your data here: ")

        birthday_data = birthday_str.split(",")

        if validate_new_birthday_data(birthday_data):
            break

    #return data    
        




def validate_new_birthday_data(values):
    """
    Validates the data entered for a new birthday is valid,
    the first entry-string- is a number and can have letters, should not be more than 5 characters long.
    the second entry-string should be letters(isalpha), not more than 12 characters long.
    """  
    
    
    if :
        raise ValueError(f"Hmm, this information is very long, is it correct?")
        return False
    else: 
        return True, update_spreadsheet()
        

    


def update_spreadsheet():
    print(f"updating {month_result}...\n")
    
 



def main():
    """
    run all program functions
    """

    select_month() 
    first_user_choice() 
    #get_birthday_data()
    #add_birhday()
    #update_spreadsheet(new_birthday_data, month_result)
    
print("Welcome to your Birthday Reminder App.\n")     
main()     
