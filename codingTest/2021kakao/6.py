import copy
from collections import deque


def solution(board, r, c):
    min_ = 987654321
    visited = [[False for _ in range(4)] for _ in range(4)]
    boardCopy = []
    answer = 0
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]

    def isRange(r, c):
        if 0 <= r < 4 and 0 <= c < 4:
            return True
        return False

    def targetPosition(board, target):
        for r in range(4):
            for c in range(4):
                if board[r][c] == target:
                    return (r, c)

    def search(board, curR, curC, targetR, targetC):
        localMin = 987654321
        count = 0

        count += goto(board, curR, curC, targetR, targetC)

        curR, curC, = targetR, targetC
        target = board[curR][curC]
        board[curR][curC] = 0
        count += 1
        targetR, targetC = targetPosition(board, target)

        count += goto(board, curR, curC, targetR, targetC)
        curR, curC, = targetR, targetC
        board[curR][curC] = 0
        count += 1

        for i in range(4):
            for j in range(4):
                if board[i][j] != 0:
                    boardCopy = copy.deepcopy(board)
                    tmpCount = search(boardCopy, curR, curC, i, j)
                    if localMin > count+tmpCount:
                        localMin = count+tmpCount
        if localMin == 987654321:
            return count
        return localMin

    def goto(board, curR, curC, targetR, targetC):
        if curR == targetR and curC == targetC:
            return 0
        clickCount = 0
        visitedCopy = copy.deepcopy(visited)
        dq = deque()
        dq.append((curR, curC, clickCount))
        visitedCopy[curR][curC] = True
        while dq:
            curR, curC, clickCount = dq.popleft()
            # 방향키
            for i in range(4):
                nextR = curR + dr[i]
                nextC = curC + dc[i]
                if isRange(nextR, nextC) and visitedCopy[nextR][nextC] != True:
                    if nextR == targetR and nextC == targetC:
                        return clickCount + 1
                    dq.append((nextR, nextC, clickCount+1))

            # ctrl + 방향키
            for i in range(4):
                nextR, nextC = ctrlGo(board, curR, curC, i)
                if isRange(nextR, nextC) and visitedCopy[nextR][nextC] != True:
                    if nextR == targetR and nextC == targetC:
                        return clickCount + 1
                    dq.append((nextR, nextC, clickCount+1))

    def ctrlGo(board, r, c, i):
        curR = r
        curC = c
        nextR = r+dr[i]
        nextC = c+dc[i]
        while isRange(nextR, nextC):
            curR = nextR
            curC = nextC
            if board[curR][curC] != 0:
                break
            nextR = curR + dr[i]
            nextC = curC + dc[i]

        if curR == r and curC == c:
            return -1, -1
        return curR, curC

    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                boardCopy = copy.deepcopy(board)
                ret = search(boardCopy, r, c, i, j)
                if min_ > ret:
                    min_ = ret
    answer = min_
    return answer


print(solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]],	1,	0))
