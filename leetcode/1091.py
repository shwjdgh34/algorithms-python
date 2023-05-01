from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid):
        shortest_path_length = -1
        row = len(grid)
        col = len(grid[0])
        if grid[0][0] == 1 or grid[row-1][col-1] == 1:  # 목적지는 이렇게 안해도 되긴함. 그런데 시간을 아낄 수 있음
            return shortest_path_length

        visited = [[False] * col for _ in range(row)]
        delta = [(-1, 0), (1, 0), (0, -1), (0, 1),
                 (1, 1), (1, -1), (-1, 1), (-1, -1)]

        queue = deque()
        queue.append((0, 0, 1))
        visited[0][0] = True
        while queue:
            cur_r, cur_c, cur_path_len = queue.popleft()
            if cur_r == row - 1 and cur_c == col - 1:
                shortest_path_length = cur_path_len
                break
            for dr, dc in delta:
                next_r = cur_r + dr
                next_c = cur_c + dc
                if next_r >= 0 and next_r < row and next_c >= 0 and next_c < col:
                    if grid[next_r][next_c] == 0 and not visited[next_r][next_c]:
                        queue.append((next_r, next_c, cur_path_len + 1))
                        visited[next_r][next_c] = True

        return shortest_path_length
