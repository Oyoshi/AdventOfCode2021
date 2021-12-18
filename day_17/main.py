#!/usr/bin/python3
import math
import functools as ft

V_Y_MAX = 1000

def simulate_balistic_trajectory(target_area):
    x_range, y_range = target_area[0], target_area[1]
    x_min, x_max = x_range[0], x_range[1]
    y_min, y_max = y_range[0], y_range[1]
    v_x_min = round((math.sqrt(8 * x_min + 1) - 1) / 2)
    v_x_max = x_max
    simulation_stats = []
    for v_x in range(v_x_min, v_x_max + 1):
        for v_y in range(-1 * V_Y_MAX, V_Y_MAX):
            x, y = 0, 0
            y_sim_max = 0
            v_x_sim = v_x
            is_missed = False
            is_reached = False
            stat = {'V_X': v_x_sim, 'V_Y': v_y, 'Y_MAX': y_sim_max}
            while not (is_missed or is_reached):
                is_missed = is_missed_target_area(x, y, x_max, y_min)
                is_reached = is_inside_target_area(x, y, x_min, x_max, y_min, y_max)
                x += v_x_sim
                y += v_y
                y_sim_max = y if y > y_sim_max else y_sim_max
                v_x_sim  = v_x_sim - 1 if v_x_sim > 0 else 0 # drag
                v_y -= 1 # gravitation
            if is_reached:
                stat['Y_MAX'] = y_sim_max
                simulation_stats.append(stat)
    return simulation_stats

def is_inside_target_area(x, y, x_min, x_max, y_min, y_max):
    return x_min <= x and x <= x_max and y_min <= y and y <= y_max

def is_missed_target_area(x, y, x_max, y_min):
    return x > x_max or y < y_min

def main():
    target_area = ((138, 184), (-125, -71))
    # PART 1
    simulation_stats = simulate_balistic_trajectory(target_area)
    y_max =ft.reduce(lambda acc, cur: max(acc, cur['Y_MAX']), simulation_stats, 0)
    print(f'PART 1: {y_max}')
    unique_velocities = len(simulation_stats)
    print(f'PART 2: {unique_velocities}')

if __name__ == '__main__':
    main()
