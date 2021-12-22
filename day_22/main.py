#!/usr/bin/python3
from enum import Enum
import collections as cl

class Status(Enum):
    ON = 'on'
    OFF = 'off'

X_MIN, X_MAX = -50, 50
Y_MIN, Y_MAX = -50, 50
Z_MIN, Z_MAX = -50, 50

def load_input(file_name):
    input_data = []
    with open(file_name) as f:
        for line in f:
            splitted_line = line.rstrip().split()
            status = Status(splitted_line[0])
            x_range, y_range, z_range = splitted_line[1].split(',')
            x0, x1 = map(int, x_range.split('=')[1].split('..'))
            y0, y1 = map(int, y_range.split('=')[1].split('..'))
            z0, z1 = map(int, z_range.split('=')[1].split('..'))
            input_data.append({'status': status, 'ranges': {'x0': x0, 'x1': x1, 'y0': y0, 'y1': y1, 'z0': z0, 'z1': z1}})
    return input_data

def is_outside_initialization_procedure_area(x0, x1, y0, y1, z0, z1):
    return x0 < X_MIN or x1 > X_MAX or y0 < Y_MIN or y1 > Y_MAX or z0 < Z_MIN or z1 > Z_MAX

def reboot_procedure(procedure_steps, is_init=False):
    cubes = cl.Counter()
    for step in procedure_steps:
        status = step['status']
        ranges = tuple(step['ranges'].values())
        if is_init and is_outside_initialization_procedure_area(*ranges):
            continue
        updater = cl.Counter()
        for prev_ranges in cubes:
            intersection = compute_intersection(*ranges, *prev_ranges)
            if intersection != None:
                updater[intersection] -= cubes[prev_ranges]
        if status == Status.ON:
            updater[ranges] += 1
        cubes.update(updater)
    return cubes

def compute_intersection(x0, x1, y0, y1, z0, z1, u0, u1, v0, v1, w0, w1):
    new_x0 = max(x0, u0); new_y0 = max(y0, v0); new_z0 = max(z0, w0)
    new_x1 = min(x1, u1); new_y1 = min(y1, v1); new_z1 = min(z1, w1)
    if new_x0 <= new_x1 and new_y0 <= new_y1 and new_z0 <= new_z1:
        return new_x0, new_x1, new_y0, new_y1, new_z0, new_z1
    return None

def sum_cubes_on(cubes):
    return sum(calculate_cubes_number(*coord) * ctr for coord, ctr in cubes.items())

def calculate_cubes_number(x0, x1, y0, y1, z0, z1):
    return (x1 - x0 + 1) * (y1 - y0 + 1) * (z1 - z0 + 1)

def main():
    input_data = load_input('input.txt')
    # PART 1
    cubes_part1 = reboot_procedure(input_data, True)
    sum_cubes_part1 = sum_cubes_on(cubes_part1)
    print(f'PART 1: {sum_cubes_part1}')
    # PART 2
    cubes_part2 = reboot_procedure(input_data)
    sum_cubes_part2 = sum_cubes_on(cubes_part2)
    print(f'PART 2: {sum_cubes_part2}')

if __name__ == '__main__':
    main()
