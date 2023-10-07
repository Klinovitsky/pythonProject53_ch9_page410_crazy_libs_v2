# Chapter 9. Page 410. Helper function
def make_crazy_lib(filename):
    file = open(filename, 'r')

    text = ''

    for line in file:
        text = text + process_line(line)

    file.close()

    return text


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


# It's just for test strip method
def strip_test(line_test):
    hello = line_test.strip('!?$')
    print(line_test, hello)


def main():
    lib = make_crazy_lib('lib.txt')
    print(lib)
    # strip_test('?!fine be that ? way!!!!?$?')
    # word_2_test = "running"
    # print(word_2_test)
    # print(word_2_test[-1])


if __name__ == '__main__':
    main()
