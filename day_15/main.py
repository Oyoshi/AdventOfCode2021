#!/usr/bin/python3
import queue as qe
import copy as cp

SCALE_FACTOR = 5
RISK_LEVELS = 10
RISK_MAP = {i: j % 10 if j % 10 != 0 else 1 for i, j in zip(range(1, 10), range(2, 11))}

def load_input(file_name):
    with open(file_name) as f:
        input_data = [[int(risk) for risk in line.rstrip()] for line in f]
    return input_data

def compute_min_risk(risk_matrix):
    rows = len(risk_matrix)
    cols = len(risk_matrix[0])
    queue = qe.PriorityQueue()
    queue.put((0, (0, 0)))
    visited = {(0, 0)}
    while not queue.empty():
        acc_risk, (i, j) = queue.get()
        if i == rows - 1 and j == cols - 1:
            return acc_risk
        neighbours = compute_neighbours(i, j, rows, cols)
        for (x, y) in neighbours:
            if 0 <= x < rows and 0 <= y < cols and (x, y) not in visited:
                risk = risk_matrix[x][y]
                queue.put((acc_risk + risk, (x, y)))
                visited.add((x, y))

def compute_neighbours(i, j, i_max, j_max):
    return [(i + a[0], j + a[1]) for a in [(-1,0), (1,0), (0,-1), (0,1)] if ( (0 <= i + a[0] < i_max) and (0 <= j + a[1] < j_max))]

def scale_up_matrix(risk_matrix):
    rows = len(risk_matrix)
    cols = len(risk_matrix[0])
    extended_matrix = cp.deepcopy(risk_matrix)
    for _ in range(SCALE_FACTOR - 1):
        for i in range(rows):
            for j in range(cols):
                extended_matrix[i].append(RISK_MAP[extended_matrix[i][j + rows * _]])
    for _ in range(SCALE_FACTOR - 1):
        for i in range(rows):
            new_list = [RISK_MAP[extended_matrix[i + rows * _][j]] for j in range(cols * SCALE_FACTOR)]
            extended_matrix.append(new_list)
    return extended_matrix

def main():
    risk_matrix = load_input('input.txt')
    # PART 1
    risk_part1 = compute_min_risk(risk_matrix)
    print(f'PART 1: {risk_part1}')
    # PART 2
    risk_part2 = compute_min_risk(scale_up_matrix(risk_matrix))
    print(f'PART 2: {risk_part2}')

if __name__ == '__main__':
    main()
