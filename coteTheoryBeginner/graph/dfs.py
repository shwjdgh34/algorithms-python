graph = {
    'A': ['B', 'D', 'E'],
    'B': ['A', 'C', 'D'],
    'C': ['B'],
    'D': ['A', 'B'],
    'E': ['A']
}

graph = {...}
visited = []


def dfs(cur_v):
    visited.append(cur_v)
    for next_v in graph[cur_v]:
        if next_v not in visited:
            dfs(next_v)


dfs('A')


print(visited)
