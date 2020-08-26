# 문제풀이 & 주의할점

## numOfIsland

- DFS & BFS O(n^2)
- 이 문제에서는 checked 배열을 따로 선언을 안해도 grid 1값을 0으로 만들어줌으로써 checked를 표현할 수 있다.
- M x N 배열 선언하기

```python
checked = [[0 for i in range(N)] for j in range(M)]
```

- Error :

```python
  maxX = len(grid)

  # Add 'if grid else 0'
  # if you dont, u may get 'IndexError: list index out of range'
  maxY = len(grid[0]) if grid else 0
```

## twosum

- 완전탐색 O(n^2)
- hashmap O(n)

## trappingRainWater

- stack O(n^2)

## 주식가격

- stack O(n)
- 완전탐색 O(n^2)

## 프린터

- deque O(n^2)

## 다리를 지나는 트럭

- deque O(n)
