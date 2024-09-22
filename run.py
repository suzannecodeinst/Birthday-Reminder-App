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
    other functions
    prints the chosen month to terminal
    """
    global month_result
    if int(values) == 1:
        print("January")
        month_result = 'Jan'
        return month_result
    elif int(values) == 2:
        print("February")
        month_result = 'Feb' 
        return month_result
    elif int(values) == 3:
        print("March")
        month_result = 'March' 
        return month_result  
    elif int(values) == 4:
        print("April")
        month_result = 'April'  
        return month_result 
    elif int(values) == 5:
        print("May")
        month_result = 'May'  
        return month_result
    elif int(values) == 6:
        print("June")
        month_result = 'June'  
        return month_result
    elif int(values) == 7:
        print("July")
        month_result = 'July'  
        return month_result
    elif int(values) == 8:
        print("August")
        month_result = 'Aug'  
        return month_result
    elif int(values) == 9:
        print("September")
        month_result = 'Sept'  
        return month_result
    elif int(values) == 10:
        print("October")
        month_result = 'Oct'  
        return month_result
    elif int(values) == 11:
        print("November")
        month_result = 'Nov'  
        return month_result 
    elif int(values) == 12:
        print("December")
        month_result = 'Dec'  
        return month_result                                        
    else:
        print("You need to type between 1 and 12 to  choose a month.")
        return False 
      
        
"""
def validate_data(values):
    
    Checks user choice input is either 1 or 2.
    Raises an error if not correct input.
    
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

"""

def get_birthday_data():
    """
    gets the previously selected month from the worksheet and prints the
    data to the terminal.
    need to print the data nicer...
    """
    global month_result
    birthday = SHEET.worksheet(month_result)
    birthday_detail = birthday.get_all_values()
    print(f"All birthdays in {month_result} are ...")
    print(birthday_detail)


def add_birthday_date():
    """
    Asks user for new birthday data
    enter a date, validates data
    if ok, progress to name input
    """
    #global b_date
    #error_date = "You must enter a number and a name."
    #print(f"Would you like to add a new  birthday to {month_result}?")
    #print("Please enter the date of the birthday you would like to add, followed by the name.")
    print(f"Would you like to add a new  birthday to {month_result}?")
    print("Data should be one date and a name, separated a comma.")
    print("Example: 21st, Garry\n")
         
    while True:    
        
        b_date = input("Enter a number and a name here:")
        birthday_data = b_date.split(",")

        if validate_new_birthday_data(birthday_data):
            break
        
    return birthday_data

def validate_new_birthday_data(str):

    """
    checks if there are two strings in the input,
    returns false if only one, or more than 2
    """
    if len(str) < 2:
        print("please try again")
        return False
    elif len(str) > 2:
        print("please try again")
        return False 
    else: 
        return True      
    

    
    
                   

def update_worksheet(data, worksheet):
    """
    Receives a list of integers to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    

    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully\n")      


def main():
    """
    run all program functions
    """

    select_month()  
    get_birthday_data()
    #add_birthday_date()
    new_birthday = add_birthday_date()
    update_worksheet(new_birthday, month_result)
    #birthday_result = []    
    #birthday_result.append([add_birthday_date, add_birthday_name]) 
    
    
print("Welcome to your Birthday Reminder App.\n")     
main()     
