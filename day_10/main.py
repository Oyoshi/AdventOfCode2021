#!/usr/bin/python3
import functools as ft

SYMBOL_LOOKUP_TABLE = {
    ')' : 3,
    ']' : 57,
    '}' : 1197,
    '>' : 25137,
}

def load_input(file_name):
    with open(file_name) as f:
        input_data = [[char for char in line.rstrip('\r\n')] for line in f]
    return input_data

def calculate_syntax_error_score(input):
    illegal_chars = []
    for line in input:
        stack = []
        idx = 0
        find_first = False
        while not find_first and idx < len(line):
            bracket = line[idx]
            if is_left_bracket(bracket):
                stack.append(bracket)
            else:
                left_bracket = stack.pop()
                if get_corresponding_right_bracket(left_bracket) != bracket:
                    illegal_chars.append(bracket)
            idx += 1
    return ft.reduce(lambda x, y: x + SYMBOL_LOOKUP_TABLE[y], illegal_chars, 0)

def is_left_bracket(char):
    return char == '(' or char == '[' or char == '{' or char == '<'

def get_corresponding_right_bracket(char):
    match char:
        case '(':
            return ')'
        case '[':
            return ']'
        case '{':
            return '}'
        case '<':
            return '>'

def main():
    input_data = load_input('input.txt')
    # PART 1
    syntax_error_score = calculate_syntax_error_score(input_data)
    print(f'PART 1: {syntax_error_score}')

if __name__ == '__main__':
    main()
