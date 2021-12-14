#!/usr/bin/python3
import itertools as it
import copy as cp

STEPS_PART_1 = 10
STEPS_PART_2 = 40

def load_input(file_name):
    rules = {}
    with open(file_name) as f:
        is_first_line = True
        for line in f:
            if is_first_line:
                polymer_template = [char for char in line.rstrip()]
                is_first_line = False
            elif not line.isspace():
                splitted_line = line.split(' -> ')
                rules[splitted_line[0]] = splitted_line[1].rstrip()
    return polymer_template, rules

def simulate_polymerization(polymer, rules, steps):
    pairs_counter = generate_pairs_counter(rules)
    for p in generate_pairs(polymer):
        pair = p[0] + p[1]
        pairs_counter[pair] += 1
    for _ in range(steps):
        inserts = cp.deepcopy(pairs_counter)
        for pair in inserts:
            pair_count = inserts[pair]
            pairs_counter[pair[0] + rules[pair]] += pair_count
            pairs_counter[rules[pair] + pair[1]] += pair_count
            pairs_counter[pair] -= pair_count
    chars_counter = {}
    for pair in pairs_counter.keys():
        p0, p1 = pair[0], pair[1]
        if p0 not in chars_counter.keys():
            chars_counter[p0] = 0
        if p1 not in chars_counter.keys():
            chars_counter[p1] = 0
        chars_counter[p0] += pairs_counter[pair]
        chars_counter[p1] += pairs_counter[pair]
    for char in chars_counter:
        chars_counter[char] = chars_counter[char] // 2 if chars_counter[char] % 2 == 0 else (chars_counter[char] + 1) // 2
    max_char, min_char = max(chars_counter.values()), min(chars_counter.values())
    return max_char, min_char

def generate_pairs_counter(pairs_insertion):
    return {key : 0 for key in pairs_insertion.keys()}

def generate_pairs(iterable_input):
    return transform_by_window_sliding(iterable_input, 2)

# TODO - used in day_01, move into utils
def transform_by_window_sliding(iterable_input, size):
    iterators = it.tee(iterable_input, size)
    iterators = [it.islice(iterator, i, None) for i, iterator in enumerate(iterators)]
    yield from zip(*iterators)

def main():
    polymer, rules = load_input('input.txt')
    # PART 1
    most_common_char, least_common_char = simulate_polymerization(polymer, rules, STEPS_PART_1)
    print(f'PART 1: {most_common_char - least_common_char}')
    # PART 2
    most_common_char, least_common_char = simulate_polymerization(polymer, rules, STEPS_PART_2)
    print(f'PART 2: {most_common_char - least_common_char}')

if __name__ == '__main__':
    main()
