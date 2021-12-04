#!/usr/bin/python3

# TODO - general refactor needed
def load_input(file_name):
    with open(file_name) as f:
        tmp_data = [[char for char in line.rstrip('\r\n')] for line in f]
    input_data = matrix_traspose(tmp_data)
    return input_data

def matrix_traspose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    res = [[None for _ in range(rows)] for _ in range(cols)]
    for i in range(cols):
        for j in range(rows):
            res[i][j] = matrix[j][i]
    return res

def most_common_bit(binary_sequence):
    zeros, ones = count_bits(binary_sequence, range(0, len(binary_sequence)), '0'), count_bits(binary_sequence, range(0, len(binary_sequence)), '1')
    return '0' if len(zeros) > len(ones) else '1'

def count_bits(binary_sequence, indices, target):
    return [i for i in indices if binary_sequence[i] == target]

def compute_gamma_and_epsilon_rates(binary_matrix):
    gamma_raw = [most_common_bit(bits) for bits in binary_matrix]
    epsilon_raw = ['0' if bit == '1' else '1' for bit in gamma_raw]
    gamma = int(''.join(gamma_raw), 2)
    epsilon = int(''.join(epsilon_raw), 2)
    return gamma, epsilon

def compute_oxygen_generator_rating(binary_matrix):
    indices = range(len(binary_matrix[0]))
    cols = len(binary_matrix)
    idx = 0
    while(len(indices) != 1 and idx < cols):
        bits = binary_matrix[idx]
        zeros, ones = count_bits(bits, indices, '0'), count_bits(bits, indices, '1')
        indices = ones if len(zeros) <= len(ones) else zeros
        idx = idx + 1
    oxygen_generator_ratings = int(''.join([bits[indices[0]] for bits in binary_matrix]), 2)
    return oxygen_generator_ratings

def compute_CO2_scrubber_rating(binary_matrix):
    indices = range(len(binary_matrix[0]))
    cols = len(binary_matrix)
    idx = 0
    while(len(indices) != 1 and idx < cols):
        bits = binary_matrix[idx]
        zeros, ones = count_bits(bits, indices, '0'), count_bits(bits, indices, '1')
        indices = zeros if len(zeros) <= len(ones) else ones
        idx = idx + 1
    return int(''.join([bits[indices[0]] for bits in binary_matrix]), 2)

def main():
    input_data = load_input('input.txt')
    # PART 1
    gamma, epsilon = compute_gamma_and_epsilon_rates(input_data)
    print(f'PART 1: {gamma * epsilon}')
    # PART 2
    oxygen_generator_rating = compute_oxygen_generator_rating(input_data)
    co2_scrubber_ratings = compute_CO2_scrubber_rating(input_data)
    print(f'PART 2: {oxygen_generator_rating * co2_scrubber_ratings}')

if __name__ == '__main__':
    main()
