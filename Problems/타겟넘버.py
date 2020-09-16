def solution(numbers, target):
    answer = 0
    global count
    count = 0
    l = len(numbers)

    def dfs(sum_, n):
        global count
        if n == l:
            if target == sum_:
                count += 1
            return

        dfs(sum_ + numbers[n], n + 1)
        dfs(sum_ - numbers[n], n + 1)

    dfs(0, 0)
    answer = count
    return answer


print(solution([1, 1, 1, 1, 1], 3))
