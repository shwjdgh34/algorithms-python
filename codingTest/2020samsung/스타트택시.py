from copy import deepcopy
from collections import deque


# class Car:
#     def __init__(self, x, y, fuel, board, client_map, goal_map):
#         self.fuel = fuel
#         self.x = x
#         self.y = y
#         self.board = board
#         self.client_map = client_map
#         self.goal_map = goal_map

#     def searchClientFuel(fuel):
#         self.fuel -= fuel
#         if self.fuel <= 0:
#             return False
#         else:
#             return True

#     def goGoalFuel(fuel):
#         self.fuel -= fuel
#         if self.fuel < 0:
#             return False
#         else:
#             self.fuel += fuel*2
#             return True

def solution(n, m, fuel, board, x, y, client):
    # car = Car(x, y, fuel, board, client_map, goal_map)
    global myFuel
    myFuel = fuel
    x -= 1
    y -= 1
    client_map = deepcopy(board)
    goal_map = deepcopy(board)
    d = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    for i, info in enumerate(client):
        client_map[info[0]-1][info[1]-1] = i+2
        goal_map[info[2]-1][info[3]-1] = i+2

    def is_range(x, y):
        if 0 <= x < n and 0 <= y < n:
            return True
        else:
            return False

    def searchClient(x, y):
        global myFuel
        check_map = deepcopy(board)
        dq = deque()
        f = 0
        dq.append((x, y, f+1))
        check_map[x][y] = 1
        if client_map[x][y] != 0:
            goal = client_map[x][y]
            client_map[x][y] = 0
            return x, y, goal

        while dq:
            cur_x, cur_y, f = dq.popleft()
            for dx, dy in d:
                next_x, next_y = cur_x+dx, cur_y+dy
                if is_range(next_x, next_y) and check_map[next_x][next_y] != 1:
                    check_map[next_x][next_y] = 1
                    if client_map[next_x][next_y] != 0:
                        goal = client_map[next_x][next_y]
                        client_map[next_x][next_y] = 0
                        myFuel -= f
                        if myFuel < 0:
                            return -1, -1, -1
                        else:
                            return next_x, next_y, goal
                    dq.append((next_x, next_y, f+1))
        return -1, -1, -1

    def go_goal(x, y, goal):
        global myFuel
        check_map = deepcopy(board)
        dq = deque()
        f = 0
        dq.append((x, y, f+1))
        check_map[x][y] = 1
        if goal_map[x][y] == goal:
            goal_map[x][y] = 0
            return x, y
        while dq:
            x, y, f = dq.popleft()
            for dx, dy in d:
                next_x, next_y = x+dx, y+dy
                if is_range(next_x, next_y) and check_map[next_x][next_y] != 1:
                    check_map[next_x][next_y] = 1
                    if goal_map[next_x][next_y] == goal:
                        goal_map[next_x][next_y] = 0
                        myFuel -= f
                        if myFuel < 0:
                            return -1, -1
                        else:
                            myFuel += f*2
                            return next_x, next_y
                    dq.append((next_x, next_y, f+1))

    for i in range(m):
        (x, y, goal) = searchClient(x, y)
        if x == -1:
            return -1
        x, y = go_goal(x, y, goal)
        if x == -1:
            return -1
    return myFuel


n, m, f = map(int, input().split())
print(n,m,f)
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

x, y = map(int, input().split())

arr2 = []
for i in range(m):
    arr2.append(list(map(int, input().split())))

print(solution(n, m, f, arr, x, y, arr2))

# print(solution(6, 3, 15, [[0, 0, 1, 0, 0, 0],
#                           [0, 0, 1, 0, 0, 0],
#                           [0, 0, 0, 0, 0, 0],
#                           [0, 0, 0, 0, 0, 0],
#                           [0, 0, 0, 0, 1, 0],
#                           [0, 0, 0, 1, 0, 0]], 6, 5, [[2, 2, 5, 6],
#                                                       [5, 4, 1, 6],
#                                                       [4, 2, 3, 5]]))
