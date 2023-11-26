# Read Word List
def read_word_list(file_path='word-list.txt'):
    # Read words from the specified file and return a list
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words
