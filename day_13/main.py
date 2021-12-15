#!/usr/bin/python3

def load_input(file_name):
    with open(file_name) as f:
        dots = []
        folds = []
        fold_instructions = False
        for line in f:
            if line.isspace():
                fold_instructions = True
            elif not fold_instructions:
                coord = line.rstrip().split(',')
                dots.append((int(coord[0]), int(coord[1])))
            else:
                splitted_fold = line.rstrip().split()
                fold_coord = splitted_fold[2].split('=')
                folds.append({'axis': fold_coord[0], 'value': int(fold_coord[1])})
    return dots, folds

def fold_paper(dots, folds_instruction):
    unique_dots = set(dots)
    for fold in folds_instruction:
        axis = fold['axis']
        value = fold['value']
        filtered_dots_to_tranform = filter(lambda d: d[0] > value if axis == 'x' else d[1] > value, unique_dots)
        filtered_dots_to_stay = set(filter(lambda d: d[0] < value if axis == 'x' else d[1] < value, unique_dots))
        for fd in filtered_dots_to_tranform:
            new_dot = (2 * value - fd[0], fd[1]) if axis == 'x' else (fd[0], 2 * value - fd[1])
            filtered_dots_to_stay.add(new_dot)
        unique_dots = filtered_dots_to_stay
    return unique_dots

def print_dots(dots):
    x_min, y_min = min(dots)
    x_max, y_max = max(dots)
    screen = [[' ' for _ in range(x_min, x_max + 1)] for _ in range(y_min, y_max + 1)]
    for d in sorted(dots):
        screen[d[1]][d[0]] = '#'
    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            print(screen[y][x], end='')
        print()

def main():
    dots, folds = load_input('input.txt')
    # PART 1
    dots_part1 = fold_paper(dots, folds[:1])
    print(f'PART 1: {len(dots_part1)}')
    # PART 2
    print('PART 2')
    dots_part2 = fold_paper(dots, folds)
    print_dots(dots_part2)

if __name__ == '__main__':
    main()
