# Chapter 9. Page 410. Helper function
# Run this program in cmd (see below):
# cd C:\Users\User\PycharmProjects\pythonProject53_ch9_page410_crazy_libs_v2
# Python3 main.py lib.txt
import sys


def make_crazy_lib(filename):
    # If it encounters a file exception it will return None.
    try:    # exception for wrong file name, change name lib.txt to test it
        file = open(filename, 'r')
        text = ''

        for line in file:
            text = text + process_line(line)
        file.close()

        return text
    except FileNotFoundError:
        print("Sorry, couldn't find", filename + '.')
    except IsADirectoryError:
        print("Sorry", filename, 'is a directory.')
    except:
        print("Sorry, could not read", filename)


placeholders = ['NOUN', 'ADJECTIVE', 'VERB_ING', 'VERB']


def process_line(line):
    global placeholders
    processed_line = ''

    words = line.split()

    for word in words:
        stripped = word.strip(',.!?:;')
        # The strip() method removes characters from both left and right based on the argument
        # (a string specifying the set of characters to be removed).

        if stripped in placeholders:
            answer = input('Enter a ' + stripped + ':')
            processed_line = processed_line + answer
            if word[-1] in ',.!?:;':  # add the punctuation back
                processed_line = processed_line + word[-1] + ' '
            else:
                processed_line = processed_line + ' '
        else:
            processed_line = processed_line + word + ' '

    return processed_line + '\n'


def save_crazy_lib(filename, text):  # test comment
    try:
        file = open(filename, 'w')
        file.write(text)
        file.close()
    except:
        print("Sorry, couldn't write file", filename)


# It's just for test strip method
def strip_test(line_test):
    hello = line_test.strip('!?$')
    print(line_test, hello)


def main():
    if len(sys.argv) != 2:      # The amount of arguments in command line
        print("main.py <filename>")
    else:
        filename = sys.argv[1]
        lib = make_crazy_lib(filename)
        # If function make_crazy_lib() encounters a file exception (wrong filename) it will return None. Page 421.
        if (lib != None):
            save_crazy_lib('crazy_' + filename, lib)
    # filename = 'lib.txt'
        # print(lib)
    # strip_test('?!fine be that ? way!!!!?$?')
    # word_2_test = "running"
    # print(word_2_test)
    # print(word_2_test[-1])


if __name__ == '__main__':
    main()
