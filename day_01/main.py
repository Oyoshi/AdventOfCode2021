#!/usr/bin/python3
import itertools as it

def load_input(file_name):
    with open(file_name) as f:
        input_data = [int(val) for val in f]
    return input_data

'''
Transform some iterable e.g. list from [a0, a1, a2, a3, ...] into list of tuples.

:param iterable iterable_input: iterable object which will be transformed into list of tuples
:param int size: size of each tuple

match size | 0 -> []
           | 1 -> [a0, a1, a2, a3, ...] - original input
           | 2 -> [(a0, a1), (a1, a2), (a2, a3), ...] - pairs
           | 3 -> [(a0, a1, a2), (a1, a2, a3), (a2, a3, a4), ...] - triplets
           ...
'''
def transform_by_window_sliding(iterable_input, size):
    iterators = it.tee(iterable_input, size)
    iterators = [it.islice(iterator, i, None) for i, iterator in enumerate(iterators)]
    yield from zip(*iterators)

def count_increasing_elements(iterable_input):
    pairs = [y-x for (x, y) in it.pairwise(iterable_input)]
    return len(list(filter(lambda elem: elem > 0, pairs)))

def main():
    input_data = load_input('input.txt')
    # PART 1
    increasing_elements_num_1 = count_increasing_elements(input_data)
    print(f'PART 1: {increasing_elements_num_1}')
    # PART 2
    transformed_input = list(map(sum, (transform_by_window_sliding(input_data, 3))))
    increasing_elements_num_2 = count_increasing_elements(transformed_input)
    print(f'PART 2: {increasing_elements_num_2}')

if __name__ == '__main__':
    main()
