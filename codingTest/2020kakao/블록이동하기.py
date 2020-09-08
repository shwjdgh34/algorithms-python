from collections import deque


def solution(board):
    n = len(board)
    # dir & dx,dy : 0 1 2 3 동 남 서 북
    visited = [[[False for _ in range(4)] for _ in range(len(board))]
               for _ in range(len(board))]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    def canGo(x, y, d):
        x2 = x + dx[d]
        y2 = y + dy[d]
        if 0 <= x2 < n and 0 <= y2 < n:
            if board[x][y] == 0 and board[x2][y2] == 0:
                return True
        return False

    def canChangeDir(x, y, d, nextD):
        x2 = x + dx[d]
        y2 = y + dy[d]

        nextX2 = x + dx[nextD]
        nextY2 = y + dy[nextD]

        if not (0 <= x2 < n and 0 <= y2 < n):
            return False
        if not (0 <= nextX2 < n and 0 <= nextY2 < n):
            return False
        if board[nextX2][nextY2] == 1:
            return False

        # 동, 서
        if d == 0 or d == 2:
            if board[nextX2][y2] == 1:
                return False
        # 남, 북
        else:
            if board[x2][nextY2] == 1:
                return False
        return True

    visited[0][0][0] = True
    visited[dx[0]][dy[0]][2] = True
    x, y, d, t = 0, 0, 0, 0
    dq = deque()
    dq.append((x, y, d, t))

    while dq:
        (x, y, d, t) = dq.popleft()
        if (x == n-1 and y == n-1) or (x + dx[d] == n-1 and y + dy[d] == n-1):
            return t
        # x,y 기준 dir 변경! +1 or -1
        for i in [-1, 1]:
            nextD = (d + i) % 4
            if 0 <= x + dx[nextD] < n and 0 <= y + dy[nextD] < n:
                if visited[x][y][nextD] == False and canChangeDir(x, y, d, nextD):
                    visited[x][y][nextD] = True
                    dq.append((x, y, nextD, t+1))

        # x2,y2 기준 dir 변경! +1 or -1
        for i in [-1, 1]:
            counterD = (d+2) % 4
            counterX = x + dx[d]
            counterY = y + dy[d]
            nextD = (counterD + i) % 4
            if 0 <= counterX + dx[nextD] < n and 0 <= counterY + dy[nextD] < n:
                if visited[counterX][counterY][nextD] == False and canChangeDir(counterX, counterY, counterD, nextD):
                    visited[counterX][counterY][nextD] = True
                    dq.append((counterX, counterY, nextD, t+1))

        # 동서남북 이동!
        for i in range(4):
            nextX = x + dx[i]
            nextY = y + dy[i]
            if 0 <= nextX < n and 0 <= nextY < n:
                if visited[nextX][nextY][d] == False and canGo(nextX, nextY, d):
                    visited[nextX][nextY][d] = True
                    dq.append((nextX, nextY, d, t+1))


print(solution([[0, 0, 0, 1, 1],
                [0, 0, 0, 1, 0],
                [0, 1, 0, 1, 1],
                [1, 1, 0, 0, 1],
                [0, 0, 0, 0, 0]]))
