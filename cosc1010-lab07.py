# Braeden Kirby
# UWYO COSC 1010
# 10/31/2024
# Lab 07
# Lab Section: 13
# Sources, people worked with, help given to: 
# your
# comments
# here


# Prompt the user for an upper bound 
# Write a while loop that gives the factorial of that upper bound
# This will need to be a positive number
# For this you will need to check to ensure that the user entered a number
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # If a user did not enter a number output a statement saying so
# You will continue to prompt the user until a proper integer value is entered

# I can start with a while loop to find the factorials. I can make the use be able to escape the operation or return to the start through 'EXIT'

def factorial_calculator():
    while True:
        user_upper_bound = input("Please enter a positive number in order to calculate the factorial (or enter 'EXIT' to quit out): ")
        if user_upper_bound.upper() == 'EXIT':
            break
        if user_upper_bound.isdigit():
            user_upper_bound = int(user_upper_bound)
            factorial = 1
            for i in range(1, user_upper_bound + 1):
                factorial *= i
            print(f"The result of the factorial based on the given bound is {factorial}")
            break
        else:
            print("Invalid value. Please enter a positive number.")

if __name__ == "__main__":
    factorial_calculator()

print("*"*75)

# Create a while loop that prompts a user for input of an integer values
# Sum all inputs. When the user enters 'exit' (regardless of casing) end the loop
# Upon ending the loop print the sum
# Your program should accept both positive and negative input
# Remember all inputs from stdin are strings, so you will need to convert the string to an int first
# Before you convert the number you need to check to ensure that it is a numeric string
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # This will return true if every digit in your string is a numerical character
    # However, that means a string such as `-1` would return false, even though your program should accept negative values
    # This means you will need to have a check to see if `-` is first character of the string before you check if it is numerical
    # If it is in the string you will need to remove the `-` character, and know that it will be a negative number, so a subtraction from the overall sum
    # I recommend checking out: https://www.w3schools.com/python/ref_string_replace.asp to figure out how one may remove a character from a string
# All this together means you will have an intensive while loop that includes multiple if statements, likely with some nesting 
# The sum should start at 0 

def numerical_sum_calculator():

    num_sum = 0 

    while True:
        upper_bound = input("Please enter a positive integer (or type 'EXIT' to be done): ")
        if upper_bound.upper() == 'EXIT':
            print(f"Your final sum is {num_sum}")
            return
        if upper_bound.startswith('-'):
            if upper_bound[1:].isdigit():
                num_sum += int(upper_bound)
            else:
                print('Invalid value. Please enter a valid number.')
        elif upper_bound.isdigit():
            num_sum += int(upper_bound)
        else:
            print('Invalid value. Please enter a valid number.')

if __name__ == "__main__":
    numerical_sum_calculator()

print("*"*75)


# Now you will be creating a two operand calculator
# It will support the following operators: +,-,/,*,% 
# So accepted input is of the form `operand operator operand` 
# You can assume that the user is competent and will only input strings of that form 
# You will again need to verify that the operands are numerical values
# For this assume only positive integers will be entered, no need look for negative numbers 
# You will need to check the string for which operator it contains
# Once you do, you will need to remove the operands from the string
# This can be done in multiple ways:
    # You can go through the string in a loop and create a substring of the characters until an operator is reached
        # Upon reaching the operator you will switch to another substring and add all characters following to the second new string 
    # Alternatively you can use the `.split()` method to split the string around an operator: https://www.w3schools.com/python/ref_string_split.asp
# Your program will need to work with whatever spacing is given  
    # So, it should function the same for `5 + 6` as `5+6`
# Print the result of the equation
# Again, loop through prompting the user for input until `exit` in any casing is input 

def basic_calculator():

        while True:
            user_input = input("Please enter a calculation in the form of 'operand operator opernad' (or enter 'EXIT' to quit): ")
            if user_input.upper() == 'EXIT':
                return
            
            user_input = user_input.replace(" ","")
            working_operators = ["+", "-", "/", "*" ,"%"]
            operator = None

            for operat in working_operators:
                if operat in user_input:
                    operator = operat
                    break
            if operator:
                operands = user_input.split(operator)
                if len(operands) == 2 and all(op.digits() for op in operands):
                    number1 = int(operands[0])
                    number2 = int(operands[1])
                    if operator == "+":
                        resulting_value = number1 + number2
                    elif operator == "-":
                        resulting_value = number1 - number2
                    elif operator == "/":
                        if number2 != 0:
                            resulting_value = number1 / number2
                        else:
                            print("Calculator Error: Unable to Divide by Zero")
                            continue
                    elif operator == "*":
                        resulting_value = number1 * number2 
                    elif operator == "%":
                        resulting_value = number1 % number2
                    print(f"The result of the calculation is: {resulting_value}")
                else:
                    print("Invalid value. Please enter a valid calculation with two valid numbers and a valid operation.")
            else:
                print("Invalid value. Please include a valid operator. These include '+', '-', '/', '*', and '%'. Thank you.")
                    
if __name__ == "__main__":
    basic_calculator()