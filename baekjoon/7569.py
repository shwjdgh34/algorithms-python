from collections import deque
class Solution(object):
    # BFS를 해야 날짜를 세기 편하다.
    def tomato_bfs(self, input):
        queue = deque()

        m, n, h = tuple(input[0:3]) # 이거 편게 하는방법?
        tomato_box = [[[-2]*n for _ in range(m)] for _ in range(h)]
        visited = [[[False]*n for _ in range(m)] for _ in range(h)] # 이거 없어도 될듯
        last_date = 0 # 여기에 초기화 해줘야되나
        dx = [0,0,0,0,1,-1]
        dy = [1,-1,0,0,0,0]
        dz = [0,0,1,-1,0,0]

        for i in range(h):
            for j in range(m):
                for k in range(n):
                    tomato_box[i][j][k]= input[(m*n*i) + (n*j) + k + 3]

        
        for i in range(h):
            for j in range(m):
                for k in range(n):
                    if tomato_box[i][j][k] == 1 and visited[i][j][k] == False:
                        visited[i][j][k] = True
                        queue.append((i,j,k,0))
        
        while(queue):
            z,x,y,date = queue.popleft()
            last_date = date
            print(z,x,y,date)
            
            for i in range(6):
                    next_x = x + dx[i]
                    next_y = y + dy[i]
                    next_z = z + dz[i]
                    if 0 <= next_z < h and 0 <= next_x < m and 0 <= next_y < n:
                        if tomato_box[next_z][next_x][next_y] == 0 and visited[next_z][next_x][next_y] == False:
                            tomato_box[next_z][next_x][next_y] = 1
                            visited[next_z][next_x][next_y] == True
                            queue.append((next_z, next_x, next_y, date+1))
            
        for i in range(h):
            for j in range(m):
                for k in range(n):
                    if tomato_box[i][j][k] == 0:
                        return -1
        return last_date 
        

s = Solution()
# print(s.tomato_bfs([5,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]))
# print(s.tomato_bfs([5,3,1,0,-1,0,0,0,-1,-1,0,1,1,0,0,0,1,1]))
# print(s.tomato_bfs([4,3,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,-1,1,1,1,-1]))

