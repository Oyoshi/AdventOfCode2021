#!/usr/bin/python3
import functools as ft
import copy as cp

def load_input(file_name):
    with open(file_name) as f:
        input_data = ft.reduce(reducer_callback, [tuple(line.rstrip().split('-')) for line in f], {})
    return input_data

def reducer_callback(acc, cur):
    acc[cur[0]] = acc[cur[0]] + [cur[1]] if cur[0] in acc else [cur[1]]
    acc[cur[1]] = acc[cur[1]] + [cur[0]] if cur[1] in acc else [cur[0]]
    return acc

def generate_all_paths(graph, source, destination, enable_doubles):
    paths_ctr = 0
    deque = [(source, set([source]), False)]
    while len(deque) > 0:
        node, seen, visited = deque.pop(0)
        if node == destination:
            paths_ctr += 1
        else:
            for direct_children in graph[node]:
                if direct_children not in seen:
                    seen_copy = cp.copy(seen)
                    if direct_children.islower():
                        seen_copy.add(direct_children)
                    deque.append(((direct_children, seen_copy, visited)))
                elif direct_children in seen and not visited and direct_children not in [source, destination] and enable_doubles:
                    deque.append(((direct_children, seen, True)))
    return paths_ctr

def main():
    input_data = load_input('input.txt')
    # PART 1
    all_paths_part1 = generate_all_paths(input_data, "start", "end", False)
    print(f'PART 1: {all_paths_part1}')
    # PART 2
    all_paths_part2 = generate_all_paths(input_data, "start", "end", True)
    print(f'PART 2: {all_paths_part2}')

if __name__ == '__main__':
    main()
