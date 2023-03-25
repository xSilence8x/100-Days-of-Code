import calculator

print(calculator.logo)

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
def square(a, b):
    return a ** b


def calculator():
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
        "**": square,
    }

    number1 = float(input(f"Type first number: "))
    for item in operations:
            print(item)
    
    end = False
    while not end:
        operation = input(f"Pick an operation: ")
        number2 = float(input(f"Type another number: "))
    
        math_function = operations[operation] # my_function = operations["+"] >>> add
        result = math_function(number1, number2) # result = add(number1, number2)
        print(f"{number1} {operation} {number2} = {result}")
        
        answer = input(f"Do you want to continue operations with number {result}? 'y' for yes 'n' to continue v new numbers ")
        if answer == "y":
            number1 = result
        else:
            end = True
            calculator()

calculator()  
