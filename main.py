import sys
from stats import get_num_words, get_chars_dict, get_char_dict_list


def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        num_words = get_num_words(text)
        chars_dict = get_chars_dict(text)
        print('============ BOOKBOT ============')
        print(f'Analyzing book found at {book_path}...')
        print('----------- Word Count ----------')
        print(f'Found {num_words} total words')
        char_dict_list = get_char_dict_list(chars_dict)
        char_dict_list.sort(reverse=True, key=sort_on)
        print('--------- Character Count -------')
        for i in range(len(char_dict_list)):
            char = char_dict_list[i]['char']
            num = char_dict_list[i]['num']
            print(f'{char}: {num}')
        print('============= END ===============')


def get_book_text(path):
    with open(path) as f:
        return f.read()


def sort_on(items):
    return items['num']


main()
