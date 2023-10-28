from collections import defaultdict

graph = defaultdict(list)

relations_num = int(input())
for i in range(relations_num):
    relation = input().split()
    if relation[1] == '->':
        graph[relation[0]].append(relation[2])
    elif relation[1] == '??':
        graph[relation[2]].append(relation[0])
        graph[relation[0]].append(relation[2])


def dfs(node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            if node in graph[neighbor] and neighbor in graph[node]:
                continue
            dfs(neighbor, visited)

possible_spreaders = set(graph.keys())
for node in list(graph): # create a copy of the dictionary keys
    visited = set()
    dfs(node, visited)
    possible_spreaders.difference_update(visited)

# sort names by alphabetical order
for x in sorted(possible_spreaders):
    print(x)