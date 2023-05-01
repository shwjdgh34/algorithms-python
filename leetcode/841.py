from collections import deque


def canVisitAllRooms(rooms):
    # visited = set()
    # visited = {}
    visited = [False] * len(rooms)

    def bfs(v):
        queue = deque()
        queue.append(v)
        visited[v] = True
        while queue:
            cur_v = queue.popleft()
            for next_v in rooms[cur_v]:
                if not visited[next_v]:
                    queue.append(next_v)
                    visited[next_v] = True

    bfs(0)
    return all(visited)


def canVisitAllRooms(rooms):
    # visited = set()
    # visited = {}
    visited = [False] * len(rooms)

    def dfs(v):
        visited[v] = True
        for next_v in rooms[v]:
            if not visited[next_v]:  # 방 번호가 0,1,2, ... , n-1 이라서 가능한 코드
                dfs(next_v)

    dfs(0)
    return all(visited)


rooms = [[1, 3], [3, 0, 1], [2], [0]]
print(canVisitAllRooms(rooms))
