def solution(numbers):
    n = len(numbers)
    s = set()
    answer = []
    for i in range(n):
        for j in range(i+1, n):
            s.add(numbers[i] + numbers[j])
    answer = list(s)
    answer.sort()
    return answer


print(solution([2, 1, 3, 4, 1]))
