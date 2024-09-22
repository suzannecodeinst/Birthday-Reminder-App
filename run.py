
import gspread
from google.oauth2.service_account import Credentials
import sys

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
    """Asks the user to choose a month.

    asks for an input of a number from 1 to 12
    print an error if a letter is input
    """
    error = "You must enter a number between 1 and 12"
    print("Choose a month to get started")
    print("All months are numbered 1 to 12,")
    print("so January is 1, February is 2 etc.")

    while True:
        try:
            b_month = int(input("Enter a number here:\n"))
        except ValueError:
            print(error)
            continue
        if b_month in range(1, 13):
            chosen_month_data(b_month)
            break
        else:
            print(error)


def chosen_month_data(values):
    """Select chosen month worksheet from the Google Doc.

    return the correct sheet as a global variable
    pass to other functions
    print the chosen month to terminal
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


def get_birthday_data():
    """Get the previously selected month from the worksheet.

    Prints the data to the terminal.
    Code copied from Love Sandwiches.
    """
    global month_result
    birthday = SHEET.worksheet(month_result)
    birthday_detail = birthday.get_all_values()
    print(f"All birthdays in {month_result} are ...")
    print(birthday_detail)


def add_birthday_date():
    """Ask user for new birthday data.

    Enter a date and a name.
    Validate data.
    """
    print(f"Would you like to add a new  birthday to {month_result}?")
    print("Please enter a date and a name, separated by a comma.")
    print("Example: 21st, Garry\n")
    while True:
        b_date = input("Enter a number and a name here:\n")
        birthday_data = b_date.split(",")
        if validate_new_birthday_data(birthday_data):
            break
    return birthday_data


def validate_new_birthday_data(str):
    """Check there are two strings in the input.

    return false if only one or more than 2.
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
    """Receive a list of integers to be inserted into worksheet.

    Update the relevant worksheet with the data provided.
    Code copied from the love sandwiches project.
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully\n")


def main():
    """Run all program functions.
    """
    select_month()
    get_birthday_data()
    new_birthday = add_birthday_date()
    update_worksheet(new_birthday, month_result)
    userInput = input("Enter 'm' to check another month or 'x' to exit:\n")
    if userInput == "x":
        print('Goodbye.')
        sys.exit()
    else:
        main()


print("Welcome to your Birthday Reminder App.\n")
main()