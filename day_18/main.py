#!/usr/bin/env python3
import functools as ft
import itertools as it
import math

MAX_DEPTH = 4
UPPER_BOUNDARY_REGULAR_NUMBER = 10

def load_input(file_name):
    with open(file_name) as f:
        input_data = [eval(line.rstrip()) for line in f]
    return input_data

def add(lhs, rhs):
    return normalize([lhs, rhs])

def normalize(nums):
    prev = None
    while nums != prev:
        prev = nums
        nums = repeat_explosions(nums)
        nums = split(nums)
    return nums

def repeat_explosions(nums):
    prev = None
    while nums != prev:
        prev = nums
        nums = explode(nums)
    return nums

def explode(nums):
    return explode_rec(nums)[0]

def explode_rec(nums, depth = 0):
    if is_regular_number(nums):
        return nums, None
    lhs, rhs = nums
    if depth == MAX_DEPTH:
        return 0, [lhs, rhs]
    lhs, lhs_explosion = explode_rec(lhs, depth+1)
    if lhs_explosion is not None:
        rhs = fix_explode_left(rhs, lhs_explosion[1])
        return [lhs, rhs], [lhs_explosion[0], 0]
    rhs, rhs_explosion = explode_rec(rhs, depth+1)
    if rhs_explosion is not None:
        lhs = fix_explode_right(lhs, rhs_explosion[0])
        return [lhs, rhs], [0, rhs_explosion[1]]
    return [lhs, rhs], None

def is_regular_number(nums):
    return isinstance(nums, int)

def fix_explode_left(nums, add):
    if is_regular_number(nums):
        return nums + add
    lhs, rhs = nums
    lhs = fix_explode_left(lhs, add)
    return [lhs, rhs]
 
def fix_explode_right(nums, add):
    if is_regular_number(nums):
        return nums + add
    lhs, rhs = nums
    rhs = fix_explode_right(rhs, add)
    return [lhs, rhs]

def split(nums):
    return split_rec(nums)[0]

def split_rec(nums):
    if is_regular_number(nums):
        if nums >= UPPER_BOUNDARY_REGULAR_NUMBER:
            lhs = math.floor(nums / 2)
            rhs = math.ceil(nums / 2)
            return [lhs, rhs], True
        else:
            return nums, False
    lhs, rhs = nums
    lhs, finish = split_rec(lhs)
    if finish:
        return [lhs, rhs], True
    rhs, done = split_rec(rhs)
    return [lhs, rhs], done

def magnitude(nums):
    if is_regular_number(nums):
        return nums
    lhs, rhs = nums
    return 3*magnitude(lhs) + 2*magnitude(rhs)

def main():
    input_data = load_input('input.txt')
    # PART 1
    sum_magnitude = magnitude(ft.reduce(add, input_data))
    print(f'PART 1: {sum_magnitude}')
    # PART 2
    largest_two_sum = max(map(lambda p: magnitude(add(p[0], p[1])), it.permutations(input_data, 2)))
    print(f'PART 2: {largest_two_sum}')

if __name__ == '__main__':
    main()
