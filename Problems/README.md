# 문제풀이 & 주의할점

## numOfIsland

- DFS & BFS O(n^2)
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
