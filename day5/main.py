#!/usr/bin/python3
import functools as ft

def load_input(file_name):
    with open(file_name) as f:
        input_data = [[{f'{"x" if idx_in == 0 else "y"}{idx_out+1}': int(coord) for idx_in, coord in enumerate(coordinates.split(','))} for idx_out, coordinates in enumerate(line.rstrip('\r\n').split(' -> '))] for line in f]
        input_data = [ft.reduce(lambda lhs, rhs: {**lhs, **rhs}, sublist) for sublist in input_data]
    return input_data

def map_coordinates_into_lines(coordinates, filter_predicate):
    filtered = [elem for elem in filter(filter_predicate, coordinates)]
    ranges = find_ranges(filtered)
    matrix = [[0 for _ in range(ranges['xmax']+1)] for _ in range(ranges['ymax']+1)]
    for coord in filtered:
        if coord['y1'] == coord['y2']:
            x_ranges = range(coord['x1'], coord['x2']+1) if coord['x1'] < coord['x2'] else range(coord['x1'], coord['x2']-1, -1)
            for x in x_ranges:
                matrix[coord['y1']][x] = matrix[coord['y1']][x] + 1
        elif coord['x1'] == coord['x2']:
            y_ranges = range(coord['y1'], coord['y2']+1) if coord['y1'] < coord['y2'] else range(coord['y1'], coord['y2']-1, -1)
            for y in y_ranges:
                matrix[y][coord['x1']] = matrix[y][coord['x1']] + 1
        else:
            x_ranges = range(coord['x1'], coord['x2']+1) if coord['x1'] < coord['x2'] else range(coord['x1'], coord['x2']-1, -1)
            y_ranges = range(coord['y1'], coord['y2']+1) if coord['y1'] < coord['y2'] else range(coord['y1'], coord['y2']-1, -1)
            for y, x in zip(y_ranges, x_ranges):
                matrix[y][x] = matrix[y][x] + 1
    return matrix

def filter_predicate_part1(coord):
    return filter_horizontal_lines(coord) or filter_vertical_lines(coord)

def filter_predicate_part2(coord):
    return filter_horizontal_lines(coord) or filter_vertical_lines(coord) or filter_diagonal_lines(coord)

def filter_horizontal_lines(coord):
    return coord['x1'] == coord['x2']

def filter_vertical_lines(coord):
    return coord['y1'] == coord['y2']

def filter_diagonal_lines(coord):
    return abs(coord['y1'] - coord['y2']) == abs(coord['x1'] - coord['x2'])

def find_ranges(coordinates):
    return ft.reduce(callback, coordinates, {'xmax': 0, 'ymax': 0})

def callback(acc, current):
    current_x_max = current['x1'] if current['x1'] > current['x2'] else current['x2']
    if current_x_max > acc['xmax']:
        acc['xmax'] = current_x_max
    current_y_max = current['y1'] if current['y1'] > current['y2'] else current['y2']
    if current_y_max > acc['ymax']:
        acc['ymax'] = current_y_max
    return acc

def calcuate_overlaping_points(matrix):
    return sum(map(lambda elem : elem > 1, (e for row in matrix for e in row)))

def main():
    input_data = load_input('input.txt')
    # PART 1
    matrix_1 = map_coordinates_into_lines(input_data, filter_predicate_part1)
    points_num_1 = calcuate_overlaping_points(matrix_1)
    print(f'PART 1: {points_num_1}')
    # PART 2
    matrix_2 = map_coordinates_into_lines(input_data, filter_predicate_part2)
    points_num_2 = calcuate_overlaping_points(matrix_2)
    print(f'PART 2: {points_num_2}')

if __name__ == '__main__':
    main()
