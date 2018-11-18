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


if __name__ == "__main__":
    number_input()