"""
Title: damir_calculator.py
Date: November 3, 2022
Author: Jamal Eddine Damir
Description: Python code that performs calculations
             through functions and prints the results as a string value
Sources: W3Schools.com
"""

def add(num1,num2):
    return num1 + num2

def subtract(num1,num2):
    return num1 - num2

def divide(num1, num2):
    return num1 / num2

def multiply(num1,num2):
    return num1 * num2


add_num1 = 3
add_num2 = 6
subtract_num1 = 10
subtract_num2 = 6
divide_num1 = 8
divide_num2 = 2
multiply_num1 = 10
multiply_num2 = 2

sum = str(add(add_num1, add_num2))
difference = str(subtract(subtract_num1, subtract_num2))
division = str(divide(divide_num1, divide_num2))
multiplication = str(multiply(multiply_num1, multiply_num2))

output = str(add_num1) " + " str(add_num2) " is " + sum + ".\n"

print(output)



