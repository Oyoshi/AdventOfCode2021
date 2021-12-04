#!/usr/bin/python3

def load_input(file_name):
    with open(file_name) as f:
        tmp_data = [[char for char in line.rstrip('\r\n')] for line in f]
    input_data = transpose(tmp_data)
    return input_data

def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    res = [[None for _ in range(rows)] for _ in range(cols)]
    for i in range(cols):
        for j in range(rows):
            res[i][j] = matrix[j][i]
    return res

def count_bits(binary_sequence, indices, target):
    return [i for i in indices if binary_sequence[i] == target]

def most_common_bit(binary_sequence):
    zeros, ones = count_bits(binary_sequence, range(len(binary_sequence)), '0'), count_bits(binary_sequence, range(len(binary_sequence)), '1')
    return '0' if len(zeros) > len(ones) else '1'

def compute_gamma_and_epsilon_rates(binary_matrix):
    gamma_raw = [most_common_bit(bits) for bits in binary_matrix]
    epsilon_raw = ['0' if bit == '1' else '1' for bit in gamma_raw]
    gamma = parse_binary_list_into_integer(gamma_raw)
    epsilon = parse_binary_list_into_integer(epsilon_raw)
    return gamma, epsilon

def compute_oxygen_generator_and_CO2_scrubber_ratings(binary_matrix):
    most_common_indices = range(len(binary_matrix[0]))
    least_common_indices = range(len(binary_matrix[0]))
    cols = len(binary_matrix)
    idx = 0
    while((len(most_common_indices) != 1 or len(least_common_indices) != 1) and idx < cols):
        bits = binary_matrix[idx]
        zeros_mc, ones_mc = count_bits(bits, most_common_indices, '0'), count_bits(bits, most_common_indices, '1')
        if len(most_common_indices) !=  1:
            most_common_indices = ones_mc if len(zeros_mc) <= len(ones_mc) else zeros_mc
        zeros_lc, ones_lc = count_bits(bits, least_common_indices, '0'), count_bits(bits, least_common_indices, '1')
        if len(least_common_indices) != 1:
            least_common_indices = zeros_lc if len(zeros_lc) <= len(ones_lc) else ones_lc
        idx = idx + 1
    oxygen_generator_rating_raw = [bits[most_common_indices[0]] for bits in binary_matrix]
    oxygen_generator_rating = parse_binary_list_into_integer(oxygen_generator_rating_raw)
    co2_scrubber_rating_raw = [bits[least_common_indices[0]] for bits in binary_matrix]
    co2_scrubber_rating = parse_binary_list_into_integer(co2_scrubber_rating_raw)
    return oxygen_generator_rating, co2_scrubber_rating

def parse_binary_list_into_integer(iterable):
    return int(''.join(iterable), 2)

def main():
    input_data = load_input('input.txt')
    # PART 1
    gamma, epsilon = compute_gamma_and_epsilon_rates(input_data)
    print(f'PART 1: {gamma * epsilon}')
    # PART 2
    oxygen_generator_rating, co2_scrubber_rating = compute_oxygen_generator_and_CO2_scrubber_ratings(input_data)
    print(f'PART 2: {oxygen_generator_rating * co2_scrubber_rating}')

if __name__ == '__main__':
    main()
