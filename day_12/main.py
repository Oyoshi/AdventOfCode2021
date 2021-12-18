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

def generate_all_paths(graph, source, destination, generate_all_paths_helper):
    visited = {k: False for k in graph}
    return generate_all_paths_helper(graph, source, destination, visited)

def generate_all_paths_helper_part1(graph, vertex, destination, visited, all_paths = [], path = []):
    if vertex.islower():
        visited[vertex] = True
    path.append(vertex)
    if vertex == destination:
        all_paths.append(cp.deepcopy(path))
    else:
        for v in graph[vertex]:
            if visited[v] == False:
                generate_all_paths_helper_part1(graph, v, destination, visited, all_paths, path)
                visited[v] = False
    return all_paths

def main():
    input_data = load_input('input.txt')
    # PART 1
    all_paths_part1 = generate_all_paths(input_data, "start", "end", generate_all_paths_helper_part1)
    print(f'PART 1: {len(all_paths_part1)}')

if __name__ == '__main__':
    main()
