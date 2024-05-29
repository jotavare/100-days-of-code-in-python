#create a function that check if it's leap year or not
def is_leap(year):
    """Take the inputed year and output True if is
    leap year and False if is not leap year."""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


#create a function that will write the correct number of days
def days_in_month(year, month):
    """Take the inputed year and month, check if
    the month is not > 12 or < 1. Also, will use
    the function is_leap() and output the correct
    number of days"""
    if month > 12 or month < 1:
        return "Invalid month."
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) is True and month == 2:
        return 29
    return month_days[month - 1]


#print welcome messsage
print(
    "Type the year and month you want to check (e.g. year = 2145) (e.g. month = 3)."
)
print("This will also check if it's a leap year or not a leap year.")

#ask the user for inputs and print result
year = int(input("Enter a Year: "))
month = int(input("Enter a Month: "))
days = days_in_month(year, month)
print(f"Result: {days} Days")

#print message based on is_leap True or False
if is_leap(year):
    print("It's a leap year.")
else:
    print("It's not leap year.")
