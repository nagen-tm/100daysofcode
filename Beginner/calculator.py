# operation functions and dictionary
def add(n1, n2):
    return n1 +n2
def subtract(n1, n2):
    return n1 - n2
def divide(n1, n2):
    return n1 / n2
def multiply(n1, n2):
    return n1 * n2

# syntax note: functions in a dictionary don't need ()
operations = {
    "+": add, 
    "-": subtract, 
    "/": divide, 
    "*": multiply
}

# to put the operation options on one line
options = ""
for operation in operations:
    options += f"{operation} "

# recursion to reuse calculator
def calculator():
    keep_calculating = True
    num1 = float(input("What's your first number?: "))
    print(options)
    while keep_calculating:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        # syntax note: dictionary[KEY](function_parameters) to use the funtion in value
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        # keep calculating from the first result
        continue_calc = input(f"Type 'y' to continue with {answer}, or press any key to start over: ").lower()
        if continue_calc == 'y':
            num1 = answer
        else:
            keep_calculating = False
            calculator()

calculator()