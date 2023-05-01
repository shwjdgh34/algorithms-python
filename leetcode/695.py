from collections import deque

class Solution(object):
    def maxAreaOfIsland(self, grid):
        row = len(grid)
        col = len(grid[0])
        
        ret = 0
        def bfs(x, y):
            size = 0
            
            q = deque()
            q.append((x,y))
            grid[x][y] = 0
            size += 1
            
            
            dx = [0,0,1,-1]
            dy = [1,-1, 0,0]

            while q:
                next_x,next_y = q.popleft()
                for i in range(4):
                    next_x = x + dx[i]
                    next_y = y + dy[i]
                    
                    if next_x >= 0 and next_y >= 0 and next_x < row and next_y < col:
                        if grid[next_x][next_y] == 1:
                            q.append((next_x,next_y))
                            grid[next_x][next_y] = 0
                            size += 1
            return size
                    
                    



        for x in range(row):
            for y in range(col):
                if grid[x][y] == 1:
                    ret = max(ret, bfs(x,y))
        return ret

s = Solution()
print(s.maxAreaOfIsland(grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))
        