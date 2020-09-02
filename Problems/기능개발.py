import math


def solution(progresses, speeds):

    n = len(progresses)
    answer = []
    term = [0] * n
    for i in range(n):
        term[i] = math.ceil((100 - progresses[i]) / speeds[i])

    i = 0
    while i < n:
        count = 1
        while i + count < n and term[i] >= term[i + count]:
            count += 1
        i += count
        answer.append(count)

    return answer


print(solution(	[93, 30, 55], [1, 30, 5]))
