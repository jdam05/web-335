#Title: damir_hobbies.py
#Date: November 19, 2022
#Author: Jamal Eddine Damir
#Description: Python code demonstrating the use of lists and "for loops" with
#             conditional statements.
#Sources:
# W3Schools.com

# Creating a list of hobbies
hobbies = ["gaming", "fishing", "playing guitar", "traveling", "watching soccer"]

# Iterating over the hobbies list and printing items to the console
for hobby in hobbies:
    print(hobby)

# Creating a list of days
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Iterating over the days list and displaying a message depending on the condition
for day in days:
    if day == "Saturday" or day == "Sunday":
        print("You are off today! Enjoy your hobbies!")
    else:
        print(day + " is a work day!")

