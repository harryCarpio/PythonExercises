"""
Write a Python program that asks the user for their birth date and prints the user’s current age in years, months, and days.
Sample output: You are 25 years, 4 months, and 22 days old
"""
from datetime import date

in_birth_date = input("Enter your birth date (YYYY-mm-dd): ")

birth_date_parts = in_birth_date.split("-")
birth_year = int(birth_date_parts[0])
birth_month = int(birth_date_parts[1])
birth_day = int(birth_date_parts[2])

today = date.today()
birth_date = date(birth_year, birth_month, birth_day)

months = today.month - birth_date.month
years = today.year - birth_date.year
days = today.day - birth_date.day

print("You are {} years, {} months, and {} days old".format(years, months, days))
