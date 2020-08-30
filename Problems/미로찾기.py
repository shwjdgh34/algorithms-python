from collections import deque

# queue, deque
# checkMap 발상이 신박했다. False -> True
# 동서남북 접근법 : nextX, nextY = x+dx[i], y+dy[i]
# 조건문으로 가야할곳, 가지말아야할곳 판별

def solution(mapList):
    queue = deque()

    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]

    n = len(mapList)
    m = len(mapList[0])

    checkMap = [[False]*m for _ in range(n)]
    distMap = [[0]*m for _ in range(n)]

    distMap[0][0] = 1
    checkMap[0][0] = True
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nextX = x + dx[i]
            nextY = y + dy[i]

            if 0 <= nextX < n and 0 <= nextY < m:
                if mapList[nextX][nextY] == 1 and checkMap[nextX][nextY] == False:
                    distMap[nextX][nextY] = distMap[x][y] + 1
                    checkMap[nextX][nextY] = True
                    queue.append((nextX, nextY))
    for row in distMap:
        print(row)


solution([[1, 0, 1, 1, 1, 1],
          [1, 0, 1, 0, 1, 0],
          [1, 0, 1, 0, 1, 1],
          [1, 1, 1, 0, 1, 1]])