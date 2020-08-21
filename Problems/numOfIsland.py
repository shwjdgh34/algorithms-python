class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        maxX = len(grid)
        maxY = len(grid[0]) if grid else 0
        checked = [[0 for i in range(maxY)] for j in range(maxX)]

        numOfIsland = 0
        for x, r in enumerate(grid):
            for y, c in enumerate(r):
                if c == '1' and not checked[x][y]:
                    self.dfs(x, y, grid, checked, maxX, maxY)
                    numOfIsland += 1

        return numOfIsland

    def dfs(self, curX, curY, grid, checked, maxX, maxY):
        delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        checked[curX][curY] = 1

        for k in range(4):
            dx = delta[k][0]
            dy = delta[k][1]

            nextX = curX + dx
            nextY = curY + dy

            if nextX < 0 or nextY < 0 or nextX >= maxX or nextY >= maxY:
                continue
            if grid[nextX][nextY] == '1' and checked[nextX][nextY] == 0:
                checked[nextX][nextY] = 1
                self.dfs(nextX, nextY, grid, checked, maxX, maxY)


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
s = Solution()
print(s.numIslands(grid))
