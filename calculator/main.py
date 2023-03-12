# add
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2
    
def divide(num1, num2):
    return num1 / num2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

should_continue = False 

while not should_continue: 

    num1 = int(input("What is your first number? "))
    num2 = int(input("What is your second number? "))
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation from the line above. ")
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    continue_answer = input("Do you want to continue? Type 'yes' or 'no'. ").lower
    
    if continue_answer == 'no':
        should_continue = True 
    else: 
        should_continue = False
