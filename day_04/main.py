#!/usr/bin/python3
import itertools as it
import functools as ft

BOARD_SIZE = 5

def load_input(file_name):
    boards = []
    with open(file_name) as f:
        is_first_line = True
        for line in f:
            if is_first_line:
                orders = [int(order) for order in line.split(',')]
                is_first_line = False
            elif not line.isspace():
                boards.append([{'value': int(elem), 'marked': False} for elem in filter(lambda elem: elem.isdigit(), line.rstrip('\r\n').split(' '))])
        boards = [boards[idx:idx + BOARD_SIZE] for idx in range(0, len(boards), BOARD_SIZE)]
    return orders, boards

def sum_unmarked_numbers_part1(orders, boards):
    for order in orders:
        for board in boards:
            for row_idx in range(BOARD_SIZE):
                for col_idx in range(BOARD_SIZE):
                    if board[row_idx][col_idx]['value'] == order:
                        board[row_idx][col_idx]['marked'] = True
                        win_row = True
                        for col_inner_idx in range(BOARD_SIZE):
                            win_row &= board[row_idx][col_inner_idx]['marked']
                        win_col = True
                        for row_inner_idx in range(BOARD_SIZE):
                            win_col &= board[row_inner_idx][col_idx]['marked']
                        if win_row or win_col:
                            return order, ft.reduce(lambda x, y: x + y['value'], filter(lambda val: not val['marked'], it.chain.from_iterable(board)), 0)

def sum_unmarked_numbers_part2(orders, boards):
    winning_boards = []
    winning_number = None
    for order in orders:
        board_idx = 0
        while board_idx < len(boards):
            if board_idx in winning_boards:
                board_idx += 1
                continue
            board = boards[board_idx]
            row_idx = 0
            while row_idx < BOARD_SIZE:
                col_idx = 0
                while col_idx < BOARD_SIZE:
                    if board[row_idx][col_idx]['value'] == order:
                        board[row_idx][col_idx]['marked'] = True
                        win_row = True
                        for col_inner_idx in range(BOARD_SIZE):
                            win_row &= board[row_idx][col_inner_idx]['marked']
                        win_col = True
                        for row_inner_idx in range(BOARD_SIZE):
                            win_col &= board[row_inner_idx][col_idx]['marked']
                        if win_row or win_col:
                            winning_boards.append(board_idx)
                            winning_number = order
                            row_idx = col_idx = BOARD_SIZE # to stop while loops
                    col_idx += 1
                row_idx += 1
            board_idx += 1   
    return winning_number, ft.reduce(lambda x, y: x + y['value'], filter(lambda val: not val['marked'], it.chain.from_iterable(boards[winning_boards[-1]])), 0)

def main():
    orders, boards = load_input('input.txt')
    # PART 1
    winning_number_1, unmarked_numbers_sum_1 = sum_unmarked_numbers_part1(orders, boards)
    print(f'PART 1: {winning_number_1 * unmarked_numbers_sum_1}')
    # PART 2
    winning_number_2, unmarked_numbers_sum_2 = sum_unmarked_numbers_part2(orders, boards)
    print(f'PART 2: {winning_number_2 * unmarked_numbers_sum_2}')

if __name__ == '__main__':
    main()
