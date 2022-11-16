"""
Title: damir_calculator.py
Date: November 3, 2022
Author: Jamal Eddine Damir
Description: Python code that prints string value
Sources:
W3Schools.com
Description: Python code that performs calculations
             through functions and prints the results as a string value
Sources: W3Schools.com
"""

# addition function
def add(num1,num2):
    return num1 + num2

# subtraction function
def subtract(num1,num2):
    return num1 - num2

# division function
def divide(num1, num2):
    return num1 / num2

# multiplication function
def multiply(num1,num2):
    return num1 * num2

# test variables
add_num1 = 4
add_num2 = 4
subtract_num1 = 10
subtract_num2 = 6
divide_num1 = 8
divide_num2 = 2
multiply_num1 = 10
multiply_num2 = 2

# calling functions and passing test variables
sum = str(add(add_num1, add_num2))
difference = str(subtract(subtract_num1, subtract_num2))
quotient = str(divide(divide_num1, divide_num2))
product = str(multiply(multiply_num1, multiply_num2))
division = str(divide(divide_num1, divide_num2))
multiplication = str(multiply(multiply_num1, multiply_num2))

# creating output string
output = (str(add_num1) + " + " + str(add_num2) + " is " + sum + ".\n"
         + str(subtract_num1) + " - " + str(subtract_num2) + " is " + difference +  ".\n"
         + str(divide_num1) + " / " + str(divide_num2) + " is " + quotient +  ".\n"
         + str(multiply_num1) + " * " + str(multiply_num2) + " is " + product +  ".")

#printing output string
print(output)