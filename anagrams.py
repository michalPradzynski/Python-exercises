# To start a program you have to write in the terminal "python3 anagrams.py [file name with list of words]".
import sys


def words_base_import():

    if len(sys.argv) == 1:
        print('Type in a file name as a command line argument!')

    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as file:
            words = []
            for line in file:
                words.append(line)
            words = [x.strip() for x in words]
            print(len(words))

    return words


def anagrams_search(words):

    words_sorted_letters = []
    words_sorted_letters = ["".join(sorted(word)) for word in words]

    anagrams_indexes = {}
    anagrams = {}

    for i in range(len(words_sorted_letters)):
        word_1 = words_sorted_letters[i]
        for j, word in enumerate(words_sorted_letters):
            if word_1 == word:
                anagrams_indexes.update({i: j})

    anagrams = {words[key]: words[value] for key, value in anagrams_indexes.items()}

    for key, value in anagrams.items():
        if key != value:
            print("{} <-> {}".format(key, value))


if __name__ == "__main__":
    words = words_base_import()
    anagrams_search(words)
