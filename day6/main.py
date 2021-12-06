#!/usr/bin/python3

DAYS_PART_1 = 80
DAYS_PART_2 = 256
FRESH_TIMER = 9
REFRESH_TIMER = 7

def load_input(file_name):
    with open(file_name) as f:
        input_data = [int(timer.rstrip('\r\n')) for timer in f.readline().split(',')]
    return input_data

def simulate_spawns(timers, days):
    timers_groups = [0] * FRESH_TIMER
    for t in timers:
        timers_groups[t] += 1
    for d in range(days):
        timers_groups[(d + REFRESH_TIMER) % FRESH_TIMER] += timers_groups[d % FRESH_TIMER]
    return sum(timers_groups)

def main():
    input_data = load_input('input.txt')
    # PART 1
    number_of_lanternfishes_1 = simulate_spawns(input_data, DAYS_PART_1)
    print(f'PART 1: {number_of_lanternfishes_1}')
    # PART 2
    number_of_lanternfishes_2 = simulate_spawns(input_data, DAYS_PART_2)
    print(f'PART 2: {number_of_lanternfishes_2}')

if __name__ == '__main__':
    main()
