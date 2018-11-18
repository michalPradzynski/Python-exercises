# This program converts an arabic number into a roman number.


def number_input():
    while True:
        try:
            arabic_number = int(input("Please write a number from between 0 and 4000: "))
        except ValueError:
            print("Not a number!")

        if arabic_number < 0 or arabic_number > 4000:
            print("A number must from range 0 - 4000!")
        else:
            return arabic_number


def converter(list_name, index, var_1, var_2, var_3):
    if list_name[index] == "9":
            return (var_3 + var_1)
    elif list_name[index] >= "6":
        return (var_2 + var_3 * (((int(list_name[index])-5))))
    elif list_name[index] == "5":
        return (var_2)
    elif list_name[index] == "4":
        return (var_3 + var_2)
    elif list_name[index] >= "1":
        return (var_3 * (int(list_name[index])))


def get_roman_number(arabic_number):

    place_values = list(str(arabic_number))
    roman_number = []

    if len(place_values) == 4:
        roman_number.append("M" * int(place_values[0]))
        roman_number.append(converter(place_values, 1, "M", "D", "C"))
        roman_number.append(converter(place_values, 2, "C", "L", "X"))
        roman_number.append(converter(place_values, 3, "X", "V", "I"))

    elif len(place_values) == 3:
        roman_number.append(converter(place_values, 0, "M", "D", "C"))
        roman_number.append(converter(place_values, 1, "C", "L", "X"))
        roman_number.append(converter(place_values, 2, "X", "V", "I"))

    elif len(place_values) == 2:
        roman_number.append(converter(place_values, 0, "C", "L", "X"))
        roman_number.append(converter(place_values, 1, "X", "V", "I"))

    elif len(place_values) == 1:
        if place_values[0] == "0":
            roman_number.append("nulla")
        else:
            roman_number.append(converter(place_values, 0, "X", "V", "I"))

    return "".join(roman_number)


if __name__ == "__main__":
    print("The roman number: {}".format(get_roman_number(number_input())))
