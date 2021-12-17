#!/usr/bin/python3
import functools as ft
import itertools as it

UNIQUE_SEGMENTS_LENGTH = {2: 1, 3: 7, 4: 4, 7: 8}

def load_input(file_name):
    with open(file_name) as f:
        input_data = [{'patterns': line.rstrip().split('|')[0].split(), 'output': line.rstrip().split('|')[1].split()} for line in f]
    return input_data

def count_digits_with_unique_segments_number(digits):
    return ft.reduce(lambda acc, current: acc + len(list(filter(lambda o: len(o) in UNIQUE_SEGMENTS_LENGTH, current['output']))), digits, 0)

def decode_digits(digits):
    return sum([decode_digits_helper(d) for d in digits])

def decode_digits_helper(digits):
    patterns = digits['patterns']
    one = list(filter_by_length(patterns, 2))[0]
    seven = list(filter_by_length(patterns, 3))[0]
    four = list(filter_by_length(patterns, 4))[0]
    eight = list(filter_by_length(patterns, 7))[0]
    five_lengthers = list(filter_by_length(patterns, 5))
    two, rest = compare_with_target_pattern(five_lengthers, four, 2)
    five, rest = compare_with_target_pattern(list(rest), two, 2)
    three = list(rest)[0]
    six_lengthers = list(filter_by_length(patterns, 6))
    zero, rest = compare_with_target_pattern(six_lengthers, five, 1)
    nine, rest = compare_with_target_pattern(list(rest), three, 0)
    six = list(rest)[0]
    patterns_res = [zero, one, two, three, four, five, six, seven, eight, nine]
    return int(''.join([str(match_pattern(o, patterns_res)) for o in digits['output']]))

def filter_by_length(patterns, length):
    return filter(lambda p: len(p) == length, patterns)

def compare_with_target_pattern(patterns, target, diff):
    target_set = set(target)
    for p in patterns:
        pattern_set = set(p)
        if len(target_set - pattern_set) == diff:
            return p, filter(lambda pat: pat != p, patterns)

def match_pattern(output, patterns):
    return next(i for i, p in enumerate(patterns) if set(p) == set(output))

def main():
    input_data = load_input('input.txt')
    # PART 1
    digits_num = count_digits_with_unique_segments_number(input_data)
    print(f'PART 1: {digits_num}')
    # PART 2
    decoded_sum = decode_digits(input_data)
    print(f'PART 2: {decoded_sum}')

if __name__ == '__main__':
    main()
