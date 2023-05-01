def uniquePaths(m, n):
    memo = [[-1] * n for _ in range(m)]

    def dfs(r, c):

        unique_paths = 0

        if r == 0 and c == 0:
            unique_paths = 1
        if memo[r][c] == -1:
            if r-1 >= 0:
                unique_paths += dfs(r-1, c)
            if c-1 >= 0:
                unique_paths += dfs(r, c-1)
            memo[r][c] = unique_paths
        return memo[r][c]
    return dfs(m-1, n-1)


def uniquePaths(m, n):
    memo = [[-1] * n for _ in range(m)]
    for r in range(m):
        memo[r][0] = 1
    for c in range(n):
        memo[0][c] = 1

    for r in range(1, m):
        for c in range(1, n):
            memo[r][c] = memo[r-1][c] + memo[r][c-1]

    return memo[m-1][n-1]


print(uniquePaths(3, 7))
