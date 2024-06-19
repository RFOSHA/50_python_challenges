# Write a function called age_in_minutes that tells a user how
# old they are in minutes. Your code should ask the user to enter
# their year of birth, and it should return their age in minutes (by
# subtracting their year of birth from the current year). Here are
# things to look out for:
# a. The user can only input a 4-digit year of birth. For example,
# 1930 is a valid year. However, entering any number longer
# or shorter than 4 digits, should render the input invalid.
# Notify the user that they must enter a four-digit number.
# b. If a user enters a year before 1900, your code should tell
# the user that the input is invalid. If the user enters the year
# after the current year, the code should tell the user to input
# a valid year.
# The code should run until the user inputs a valid year. Your
# function should return the user's age in minutes. For example, if
# someone enters 1930 as their year of birth, your function should
# return:
# You are 48, 355, 200 minutes old.
from datetime import datetime

def age_in_minutes():
    year = int(input("Enter the year you were born as a four digit year: "))
    if len(str(year)) != 4:
        print("The year you entered is not 4 digits")
    elif year < 1900 or year > datetime.now().year:
        print("Enter a year that is equal to or greater ")
    else:
        age = (datetime.now().year - year)
        age_in_mins = (age * 365 * 1440)
        return print(f"You are {age}, which is {age_in_mins} minutes old")

age_in_minutes()


