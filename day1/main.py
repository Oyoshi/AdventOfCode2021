from itertools import islice, tee

def window_sliding_generator(iterable_input, size):
    iterators = tee(iterable_input, size)
    iterators = [islice(iterator, i, None) for i, iterator in enumerate(iterators)]
    yield from zip(*iterators)

def pairwise(iterable_input):
    a, b = tee(iterable_input)
    next(b, None)
    yield from zip(a, b)

def count_increasing_elements(iterable_input):
    pairs = [y-x for (x, y) in pairwise(iterable_input)]
    return len(list(filter(lambda elem: elem > 0, pairs)))

def main():
    # load data from a file, pass const object or use any other technique
    input_array = []
    # PART 1
    increasing_elements_num_1 = count_increasing_elements(input_array)
    print(f'PART 1: {increasing_elements_num_1}')
    # PART 2
    transformed_input = list(map(sum, (window_sliding_generator(input_array, 3))))
    increasing_elements_num_2 = count_increasing_elements(transformed_input)
    print(f'PART 2: {increasing_elements_num_2}')

if __name__ == '__main__':
    main()
