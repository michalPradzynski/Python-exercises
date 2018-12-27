# This program can do simple calculations from a single line input.

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







if __name__ == "__main__":
    abc()