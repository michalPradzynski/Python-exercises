# This program can do simple calculations from a single line input.

def add(x,y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

def calculate(x, y, symbol):
    if symbol = "+":
        add(x, y)
    elif symbol = "-":
        subtract(x, y)
    elif symbol = "*":
        multiply(x, y)
    elif symbol = "/":
        divide(x, y)
    elif symbol = "^":
        power(x, y)

def abc():
    input_equation = input("Enter your equation: ")
    equation = "".join(input_equation)
    number1 = []
    number2 = []
    symbols = ["+", "-", "*", "/"]
    sign = None

    for character in equation:
        if sign == None:
            if character.isdigit():
                number1.append(int(character))
            elif character in symbols:
                sign = character
        else:
            if character.isdigit():
                number2.append(int(character))

    print(number1)
    print(sign)
    print(number2)

    number1 = "".join(number1)
    number2 = "".join(number2)









if __name__ == "__main__":
    abc()