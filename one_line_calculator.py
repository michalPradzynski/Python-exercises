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


def calculator():
    while True:
        input_equation = input("Enter your equation: ")

        if "exit" in input_equation:
            sys.exit()

        equation = "".join(input_equation)
        number1 = []
        number2 = []
        symbols = ["+", "-", "*", "/", "^"]
        sign = None

        for character in equation:
            if sign is None:
                if character.isdigit():
                    number1.append(character)
                elif character in symbols:
                    sign = character
            else:
                if character.isdigit():
                    number2.append(character)

        if len(number1) == 0 or len(number2) == 0 or sign is None:
            print("Please write full equation!")
            continue

        print(number1, sign, number2)

        num1 = int("".join(number1))
        num2 = int("".join(number2))

        result = calculate(num1, num2, sign)

        return result


if __name__ == "__main__":
    while True:
        print(calculator())
