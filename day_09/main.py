#!/usr/bin/python3
import functools as ft

TOP_POINT_HEIGHT = 9

def load_input(file_name):
    with open(file_name) as f:
        input_data = [[int(char) for char in line.rstrip('\r\n')] for line in f]
    return input_data

def find_lowest_points(matrix):
    lowest_points_coords = []
    rows, cols = len(matrix), len(matrix[0])
    for row in range(rows):
        for col in range(cols):
            neighbours = compute_neighbours(row, col, rows, cols)
            current = matrix[row][col]
            if min([matrix[pos[0]][pos[1]] for pos in neighbours]) > current:
               lowest_points_coords.append((row, col))
    return lowest_points_coords

def find_basin_sizes(matrix, lowest_points_coords):
    basin_sizes = []
    rows, cols = len(matrix), len(matrix[0])
    for pos in lowest_points_coords:
        coords = set(find_basin_sizes_rec_helper(matrix, pos[0], pos[1], rows, cols, [(pos[0], pos[1])]))
        basin_sizes.append(len(coords))
    return basin_sizes

def find_basin_sizes_rec_helper(matrix, i ,j, i_max, j_max, coords):
    current = matrix[i][j]
    higher_neighbours = list(filter(lambda pos: (matrix[pos[0]][pos[1]] > current) and matrix[pos[0]][pos[1]] != TOP_POINT_HEIGHT, compute_neighbours(i, j, i_max, j_max)))
    coords += higher_neighbours
    for pos in higher_neighbours:
        coords = find_basin_sizes_rec_helper(matrix, pos[0], pos[1], i_max, j_max, coords)
    return coords

def compute_neighbours(i, j, i_max, j_max):
    return [(i + a[0], j + a[1]) for a in [(-1,0), (1,0), (0,-1), (0,1)] if ( (0 <= i + a[0] < i_max) and (0 <= j + a[1] < j_max))]

def main():
    input_data = load_input('input.txt')
    # PART 1
    lowest_points_coords = find_lowest_points(input_data)
    risk_level = sum([input_data[pos[0]][pos[1]] for pos in lowest_points_coords]) + len(lowest_points_coords)
    print(f'PART 1: {risk_level}')
    basin_sizes = find_basin_sizes(input_data, lowest_points_coords)
    multiplication_three_largest_basins = ft.reduce(lambda x, y: x * y, sorted(basin_sizes, reverse=True)[:3], 1)
    print(f'PART 2: {multiplication_three_largest_basins}')

if __name__ == '__main__':
    main()
