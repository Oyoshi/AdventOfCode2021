#!/usr/bin/python3
import functools as ft
from enum import Enum

class Direction(Enum):
    FORWARD = 1
    DOWN = 2
    UP = 3

def convert_string_to_enum(direction):
    match direction:
        case 'forward':
            return Direction.FORWARD
        case 'down':
            return Direction.DOWN
        case 'up':
            return Direction.UP

def load_input(file_name):
    with open(file_name) as f:
        input_data = [{'direction': convert_string_to_enum(line.split()[0]), 'value': int(line.split()[1])} for line in f]
    return input_data

def callback_1(acc, current):
    match current['direction']:
        case Direction.FORWARD:
            acc['horizontal'] = acc['horizontal'] + current['value']
        case Direction.UP:
            acc['depth'] = acc['depth'] - current['value']
        case Direction.DOWN:
            acc['depth'] = acc['depth'] + current['value']
    return acc

def callback_2(acc, current):
    match current['direction']:
        case Direction.FORWARD:
            acc['horizontal'] = acc['horizontal'] + current['value']
            acc['depth'] = acc['depth'] + acc['aim'] * current['value']
        case Direction.UP:
            acc['aim'] = acc['aim'] - current['value']
        case Direction.DOWN:
            acc['aim'] = acc['aim'] + current['value']
    return acc

def main():
    input_data = load_input('input.txt')
    # PART 1
    reduced_1 = ft.reduce(callback_1, input_data, {'horizontal': 0, 'depth': 0})
    result_1 = reduced_1['horizontal'] * reduced_1['depth']
    print(f'PART 1: {result_1}')
    # PART 2
    reduced_2 = ft.reduce(callback_2, input_data, {'horizontal': 0, 'aim': 0, 'depth': 0})
    result_2 = reduced_2['horizontal'] * reduced_2['depth']
    print(f'PART 2: {result_2}')

if __name__ == '__main__':
    main()
