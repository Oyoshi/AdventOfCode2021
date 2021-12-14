#!/usr/bin/python3
import math

def load_input(file_name):
    with open(file_name) as f:
        input_data = [int(pos) for pos in f.readline().split(',')]
    return input_data

def find_optimal_position(initial_positions, callback):
    min_val, max_val = min(initial_positions), max(initial_positions)
    optimal_sum = math.inf
    for target in range(min_val, max_val + 1):
        current_sum = sum([callback(e, target) for e in initial_positions])
        if current_sum < optimal_sum:
            optimal_sum = current_sum
    return optimal_sum

def callback_1(e, target):
    return abs(e - target)

def callback_2(e, target):
    n = abs(e - target) + 1
    return n * (n - 1) // 2

def main():
    input_data = load_input('input.txt')
    # PART 1
    optimal_sum_1 = find_optimal_position(input_data, callback_1)
    print(f'PART 1: {optimal_sum_1}')
    # PART 2
    optimal_sum_2 = find_optimal_position(input_data, callback_2)
    print(f'PART 2: {optimal_sum_2}')

if __name__ == '__main__':
    main()
