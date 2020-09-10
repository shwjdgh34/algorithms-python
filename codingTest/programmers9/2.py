def solution(n):
    triangleMap = [[0 for _ in range(n)] for _ in range(n)]
    num = [1]

    def dp(x, y):
        # go down
        triangleMap[x][y] = num[0]
        num[0] += 1
        while True:
            if x + 1 < n and triangleMap[x+1][y] == 0:
                x += 1
                triangleMap[x][y] = num[0]
                num[0] += 1
            else:
                break
        # go left
        while True:
            if y + 1 < n and triangleMap[x][y+1] == 0:
                y += 1
                triangleMap[x][y] = num[0]
                num[0] += 1
            else:
                break
        # go diag
        while True:
            if y - 1 >= 0 and x - 1 >= 0 and triangleMap[x-1][y-1] == 0:
                x -= 1
                y -= 1
                triangleMap[x][y] = num[0]
                num[0] += 1
            else:
                break

        if x+1 < n and triangleMap[x+1][y] == 0:
            dp(x+1, y)

    dp(0, 0)
    answer = []
    for i in range(n):
        for j in range(i+1):
            answer.append(triangleMap[i][j])
    return answer


print(solution(1))
