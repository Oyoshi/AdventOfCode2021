#!/usr/bin/python3
import copy as cp

STEPS_NUM = 100
MIN_ENERGY_LEVEL = 0
MAX_ENERGY_LEVEL = 10

def load_input(file_name):
    with open(file_name) as f:
        input_data = [[{'level' : int(char), 'flashed': False} for char in line.rstrip('\r\n')] for line in f]
    return input_data

def simulate_flashes(energy_levels):
    rows = len(energy_levels)
    cols = len(energy_levels[0])
    flash_counter = 0
    for _ in range(STEPS_NUM):
        stack = []
        for i in range(rows):
            for j in range(cols):
                energy_levels[i][j]['flashed'] = False # resetting state
                energy_levels[i][j]['level'] = (energy_levels[i][j]['level'] + 1) % MAX_ENERGY_LEVEL
                if energy_levels[i][j]['level'] == MIN_ENERGY_LEVEL:
                    energy_levels[i][j]['flashed'] = True
                    stack.append((i, j))
                    flash_counter += 1
        while len(stack) != 0:
            coords = stack.pop()
            neighbours = compute_neighbours(coords[0], coords[1], rows, cols)
            filtered_neighbours = filter(lambda coord: not energy_levels[coord[0]][coord[1]]['flashed'], neighbours)
            for c in filtered_neighbours:
                new_i, new_j = c[0], c[1]
                energy_levels[new_i][new_j]['level'] = (energy_levels[new_i][new_j]['level'] + 1) % MAX_ENERGY_LEVEL
                if energy_levels[new_i][new_j]['level'] == MIN_ENERGY_LEVEL:
                    energy_levels[new_i][new_j]['flashed'] = True
                    stack.append(c)
                    flash_counter += 1
    return flash_counter

def simulate_synchronizing(energy_levels):
    rows = len(energy_levels)
    cols = len(energy_levels[0])
    step = 0
    while True:
        flash_counter_per_step = 0
        stack = []
        for i in range(rows):
            for j in range(cols):
                energy_levels[i][j]['flashed'] = False # resetting state
                energy_levels[i][j]['level'] = (energy_levels[i][j]['level'] + 1) % MAX_ENERGY_LEVEL
                if energy_levels[i][j]['level'] == MIN_ENERGY_LEVEL:
                    energy_levels[i][j]['flashed'] = True
                    stack.append((i, j))
                    flash_counter_per_step += 1
        while len(stack) != 0:
            coords = stack.pop()
            neighbours = compute_neighbours(coords[0], coords[1], rows, cols)
            filtered_neighbours = filter(lambda coord: not energy_levels[coord[0]][coord[1]]['flashed'], neighbours)
            for c in filtered_neighbours:
                new_i, new_j = c[0], c[1]
                energy_levels[new_i][new_j]['level'] = (energy_levels[new_i][new_j]['level'] + 1) % MAX_ENERGY_LEVEL
                if energy_levels[new_i][new_j]['level'] == MIN_ENERGY_LEVEL:
                    energy_levels[new_i][new_j]['flashed'] = True
                    stack.append(c)
                    flash_counter_per_step += 1
        step += 1
        if flash_counter_per_step == rows * cols:
            return step

def compute_neighbours(i, j, i_max, j_max):
    return [(i + a[0], j + a[1]) for a in [(-1,-1), (-1,0), (-1,1), (1,-1), (1,0), (1,1), (0,-1), (0,1)] if ( (0 <= i + a[0] < i_max) and (0 <= j + a[1] < j_max))]

def main():
    input_data_part1 = load_input('input.txt')
    input_data_part2 = cp.deepcopy(input_data_part1)
    # PART 1
    flashes = simulate_flashes(input_data_part1)
    print(f'PART 1: {flashes}')
    # PART 2
    step_num = simulate_synchronizing(input_data_part2)
    print(f'PART 2: {step_num}')

if __name__ == '__main__':
    main()
