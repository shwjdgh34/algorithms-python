import queue
import copy


def solution(grid, d):
    n = len(grid)

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    def bfs(i, j, d, tmpGrid):
        count = 0
        q = queue.Queue()
        q.put((i, j, 0))
        count += 1
        tmpGrid[i][j] = 1
        while q.qsize():
            x, y, curD = q.get()
            if curD >= d:
                continue
            for k in range(4):
                nextX = x+dx[k]
                nextY = y+dy[k]
                if 0 <= nextX < n and 0 <= nextY < n:
                    if tmpGrid[nextX][nextY] == 0:
                        tmpGrid[nextX][nextY] = 1
                        q.put((nextX, nextY, curD+1))
                        count += 1

        return count

    maxI, maxJ = -1, -1
    maxWater = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                tmpGrid = copy.deepcopy(grid)
                output = bfs(i, j, d, tmpGrid)
                if maxWater < output:
                    maxWater = output
                    maxI, maxJ = i, j
    return maxWater


print(solution([[0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0]], 2))
