def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def square(a):
    return a ** 2

def cube(a):
    return a ** 3

def calculator():
    while True:
        print("Options: ADD, SUB, SQUARE, CUBE, EXIT")
        operator = input("Enter operation: ").strip().upper()
        if operator == "EXIT":
            print("Exiting...")
            break
        elif operator in ["ADD", "SUB"]:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            if operator == "ADD":
                print("Result:", add(a, b))
            elif operator == "SUB":
                print("Result:", sub(a, b))
        elif operator in ["SQUARE", "CUBE"]:
            a = float(input("Enter a number: "))
            if operator == "SQUARE":
                print("Result:", square(a))
            elif operator == "CUBE":
                print("Result:", cube(a))
        else:
            print("Invalid operation")

calculator()
