import sys


def words_base_import(sys.argv):

    if len(sys.argv) == 1:
        print('Type in a file name as a command line argument!')

    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as file:
            words = []
            for line in file:
                words.append(line)
            words = [x.strip() for x in words]
            print(len(words))


if __name__ == "__main__":
    words_base_import(sys.argv)
