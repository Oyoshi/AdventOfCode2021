#!/usr/bin/python3
import itertools as it

STEPS_PART_1 = 10
STEPS_PART_2 = 40

def load_input(file_name):
    pairs_insertion = {}
    with open(file_name) as f:
        is_first_line = True
        for line in f:
            if is_first_line:
                polymer_template = [char for char in line.rstrip('\r\n')]
                is_first_line = False
            elif not line.isspace():
                splitted_line = line.split(' -> ')
                pairs_insertion[splitted_line[0]] = splitted_line[1].rstrip('\r\n')
    return polymer_template, pairs_insertion

def simulate_polymerization(polymer, pairs_insertion, steps):
    # setup initial counter values
    chars_counter = generate_unique_chars_counter(pairs_insertion)
    pairs_num_boundary = calculate_number_of_pairs(polymer, steps + 1)
    for char in polymer:
        chars_counter[char] = chars_counter[char] + 1
    queue = [p for p in generate_pairs(polymer)]
    pairs_counter = len(queue)
    while pairs_counter < pairs_num_boundary and len(queue) != 0:
        pair = queue.pop(0)
        inserted = pairs_insertion[pair[0] + pair[1]]
        chars_counter[inserted] = chars_counter[inserted] + 1
        new_pair_1 = pair[0] + inserted
        new_pair_2 = inserted + pair[1]
        queue.append(new_pair_1)
        queue.append(new_pair_2)
        pairs_counter += 2
    max_char, min_char = max(chars_counter, key=chars_counter.get), min(chars_counter, key=chars_counter.get)
    return chars_counter[max_char], chars_counter[min_char]

def generate_unique_chars_counter(pairs_insertion):
    return {value : 0 for value in pairs_insertion.values()}

def generate_pairs(iterable_input):
    return transform_by_window_sliding(iterable_input, 2)

# sum (n-1)*2^k - geometric sequence
def calculate_number_of_pairs(iterable_input, steps):
    n = len(iterable_input)
    return (n - 1) * (2 ** steps - 1)

# TODO - used in day_01, move into utils
def transform_by_window_sliding(iterable_input, size):
    iterators = it.tee(iterable_input, size)
    iterators = [it.islice(iterator, i, None) for i, iterator in enumerate(iterators)]
    yield from zip(*iterators)

def main():
    polymer, pairs_insertion = load_input('input.txt')
    # PART 1
    most_common_char, least_common_char = simulate_polymerization(polymer, pairs_insertion, STEPS_PART_1)
    print(f'PART 1: {most_common_char - least_common_char}')
    # PART 2
    most_common_char, least_common_char = simulate_polymerization(polymer, pairs_insertion, STEPS_PART_2)
    print(f'PART 2: {most_common_char - least_common_char}')

if __name__ == '__main__':
    main()
