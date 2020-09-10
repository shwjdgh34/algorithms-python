# algorithms-python

## binary search

### bisect

```python
from bisect import bisect_left
arr = [1, 2, 3, 3, 4, 5]

def bs(arr, x):
    # 들어가야 하는 '제일 왼쪽' index 반환
    i = bisect_left(arr, x)
    if i != len(arr) and arr[i] == x:
        return i

    '''
    들어가야 하는 index가
      마지막 index + 1 이라면, arr에 x가 없는 것
      arr[i] == x가 아니라면, arr에 x가 없는 것
    '''
    else:                               #
        return -1
```

> [출처](https://justkode.kr/python/pygorithm-2)

### recursion

```python
def binarySearch(array, target, left, right):

    if left > right:
        return -1

    middle_idx = (left+right)//2
    middle = array[middle_idx]

    if target == middle:
        return middle_idx
    elif middle > target:
        return binarySearch(array, target, left, middle_idx-1)
    elif middle < target:
        return binarySearch(array, target, middle_idx+1, right)
```

### while loop

```python

```
