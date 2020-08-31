def solution(key, lock):
    answer = True
    n = len(lock)
    m = len(key)

    newKey = [[0] * (2*n-2+m) for _ in range(2*n-2+m)]
    rotated90 = [[0] * m for _ in range(m)]
    rotated180 = [[0] * m for _ in range(m)]
    rotated270 = [[0] * m for _ in range(m)]
    # reverseKey = [[1-c for c in r] for r in key]

    # 0
    for i in range(m):
        for j in range(m):
            newKey[n-1 + i][n-1 + j] = key[i][j]

    for i in range(n+m-1):
        for j in range(n+m-1):
            flag = True
            for x in range(n):
                for y in range(n):
                    if lock[x][y] + newKey[i+x][j+y] != 1:
                        flag = False

            if flag == True:
                return True
    # 90
    for i, r in enumerate(key):
        for j, c in enumerate(r):
            rotated90[j][m-1-i] = key[i][j]

    for i in range(m):
        for j in range(m):
            newKey[n-1 + i][n-1 + j] = rotated90[i][j]

    for i in range(n+m-1):
        for j in range(n+m-1):
            flag = True
            for x in range(n):
                for y in range(n):
                    if lock[x][y] + newKey[i+x][j+y] != 1:
                        flag = False

            if flag == True:
                return True

    # 180
    for i, r in enumerate(rotated90):
        for j, c in enumerate(r):
            rotated180[j][m-1-i] = rotated90[i][j]

    for i in range(m):
        for j in range(m):
            newKey[n-1 + i][n-1 + j] = rotated180[i][j]

    for i in range(n+m-1):
        for j in range(n+m-1):
            flag = True
            for x in range(n):
                for y in range(n):
                    if lock[x][y] + newKey[i+x][j+y] != 1:
                        flag = False

            if flag == True:
                return True

    # 270
    for i, r in enumerate(rotated180):
        for j, c in enumerate(r):
            rotated270[j][m-1-i] = rotated180[i][j]

    for i in range(m):
        for j in range(m):
            newKey[n-1 + i][n-1 + j] = rotated270[i][j]

    for i in range(n+m-1):
        for j in range(n+m-1):
            flag = True
            for x in range(n):
                for y in range(n):
                    if lock[x][y] + newKey[i+x][j+y] != 1:
                        flag = False

            if flag == True:
                return True
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],
               [[1, 0], [0, 1]]))
