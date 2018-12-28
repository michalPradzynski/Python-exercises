# This program can do simple calculations from a single line input.
import sys


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def power(x, y):
    return x ** y

def get_input():
    print("One Line Calculator v2.0")
    input_equation = input("Enter your equation: ")

        if "exit" in input_equation:
            sys.exit()

    return "".join(input_equation)


def calculate(x, y, symbol):
    if symbol == "+":
        return add(x, y)
    elif symbol == "-":
        return subtract(x, y)
    elif symbol == "*":
        return multiply(x, y)
    elif symbol == "/":
        return divide(x, y)
    elif symbol == "^":
        return power(x, y)


def simple_calculation(equation):
    number1 = []
    number2 = []
    operator = None

    for character in equation:
                if operator is None:
                    if character.isdigit():
                        number1.append(character)
                    elif character in symbols:
                        operator = character
                else:
                    if character.isdigit():
                        number2.append(character)

    num1 = int("".join(number1))
    num2 = int("".join(number2))

    simple_result = calculate(num1, num2, operator)

    return simple_result



def calculator():
    while True:
        equation = get_input()
        equation_parts = []

        symbols = ["+", "-", "*", "/", "^"]
        how_many_operators = 0
        operator = None

        for character in equation:
            if character in symbols:
                how_many_operators += 1
            if character == "*" or character == "/" or character == "^":
                pass

        if how_many_operators == 1:           
            result = simple_calculation(equation)
        elif how_many_operators > 1:
            for character in equation:
                if operator is None:
                    if character.isdigit():
                        number1.append(character)
                    elif character in symbols:
                        operator = character
                else:
                    if character.isdigit():
                        number2.append(character)
            equation_parts.append(int("".join(number1)))
            num2 = int("".join(number2))
                        


        if len(number1) == 0 or len(number2) == 0 or operator is None:
            print("Please write full equation!")
            continue

        print(number1, operator, number2)

        num1 = int("".join(number1))
        num2 = int("".join(number2))

        result = calculate(num1, num2, operator)

        return result


if __name__ == "__main__":
    while True:
        print(calculator())
