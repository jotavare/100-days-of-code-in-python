#import logo from art.py
from art import logo
from replit import clear

print(logo)


#define function add
def add(n1, n2):
    return n1 + n2


#define function subtract
def subtract(n1, n2):
    return n1 - n2


#define function multiply
def multiply(n1, n2):
    return n1 * n2


#define function divide
def divide(n1, n2):
    return n1 / n2


#define function dictionary with 4 operators
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


#define function to be used as a recursive method
def calculator():

    #ask the user for number 1 input as a float type
    num1 = float(input("What's the first number?: "))

    #print each operator from the dictionary 'operations'
    for symbol in operations:
        print(symbol)

    #define should_continue as true
    should_continue = True

    #create a loop based on should_continue bolean value
    while should_continue:
        #ask the user to choose one of the operators
        operation_symbol = input("Pick an operation: ")

        #ask the user for number 2 input as a float type
        num2 = float(input("What's the next number?: "))

        #check and use the operator from the operations dictionary
        #assign variable to first_answer that calculates the two numbers
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        #print the first_answer
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        #if the user types 'y' it will change the answer to num1
        #and it will use the new num1 and loop again
        if input(
                f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.\n"
        ) == "y":
            num1 = answer

        #if the user types anything not equal to 'y'
        #is gonna change should_continue to False
        #clear the console and print the logo
        #call the same function so it loop
        else:
            should_continue = False
            clear()
            print(logo)
            calculator()


#call the function for the first time
calculator()
