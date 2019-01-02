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


def calculate(x, y, operator):
    if operator == "+":
        return add(x, y)
    elif operator == "-":
        return subtract(x, y)
    elif operator == "*":
        return multiply(x, y)
    elif operator == "/":
        return divide(x, y)
    elif operator == "^":
        return power(x, y)


def simple_calculation(equation):
    number1 = []
    number2 = []
    operator = None

    for character in equation:
                if operator is None:
                    if character.isdigit():
                        number1.append(character)
                    elif character in arithmetic_operators:
                        operator = character
                else:
                    if character.isdigit():
                        number2.append(character)

    num1 = int("".join(number1))
    num2 = int("".join(number2))

    simple_result = calculate(num1, num2, operator)

    return simple_result


def separate_equation(equation):
    arithmetic_operators = ["+", "-", "*", "/", "^"]
    operators = []
    numbers = []
    temp_number = []

    for character in equation:
        if character.isdigit():
            temp_number.append(character)
        elif character in arithmetic_operators:
            operators.append(character)
            numbers.append(int("".join(temp_number)))
            temp_number = []

    return (operators, numbers)


def get_calculation_order(operators):
    ordered_symbols = []

    for index, symbol in enumerate(operators):
        if symbol == "^":
            ordered_symbols.append((0, symbol))
        elif symbol == "*" or symbol == "/":
            ordered_symbols.append((1, symbol))
        else:
            ordered_symbols.append((2, symbol))

    ordered_symbols.sort(key=lambda order: order[0])

    return ordered_symbols


def calculator():
    while True:
        equation = get_input()
        equation_parts = []

        arithmetic_operators = ["+", "-", "*", "/", "^"]
        how_many_operators = 0
        operator = None

        for character in equation:
            if character in arithmetic_operators:
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
                    elif character in arithmetic_operators:
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
