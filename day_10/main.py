#!/usr/bin/python3
import functools as ft
import statistics as st

ERROR_SYMBOL_LOOKUP_TABLE = {
    ')' : 3,
    ']' : 57,
    '}' : 1197,
    '>' : 25137,
}

INCOMPLETE_SYMBOL_LOOKUP_TABLE = {
    ')' : 1,
    ']' : 2,
    '}' : 3,
    '>' : 4,
}

MULTIPLICATION_FACTOR = 5

def load_input(file_name):
    with open(file_name) as f:
        input_data = [[char for char in line.rstrip('\r\n')] for line in f]
    return input_data

def calculate_syntax_error_score(input):
    illegal_chars = []
    incomplete_lines = []
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
                    find_first = True
            idx += 1
        if not find_first:
            incomplete_lines.append(line)
    return ft.reduce(lambda x, y: x + ERROR_SYMBOL_LOOKUP_TABLE[y], illegal_chars, 0), incomplete_lines

def calculate_completions_score(incomplete_lines):
    completions_scores = []
    for line in incomplete_lines:
        stack = []
        for bracket in line:
            if is_left_bracket(bracket):
                stack.append(bracket)
            else:
                stack.pop()
        completion = ''.join([get_corresponding_right_bracket(rb) for rb in reversed(stack)])
        completions_scores.append(ft.reduce(lambda x, y: MULTIPLICATION_FACTOR * x + INCOMPLETE_SYMBOL_LOOKUP_TABLE[y], completion, 0))
    return completions_scores

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
    syntax_error_score, incomplete_lines = calculate_syntax_error_score(input_data)
    print(f'PART 1: {syntax_error_score}')
    completions_scores = calculate_completions_score(incomplete_lines)
    print(f'PART 2: {st.median(completions_scores)}')

if __name__ == '__main__':
    main()
