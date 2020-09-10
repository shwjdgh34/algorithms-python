def solution(N, stages):
    tmpAnswer = [0 for _ in range(N+1)]

    for level in stages:
        tmpAnswer[level-1] += 1

    passedNum = 0
    for i in range(N+1, 0, -1):
        passedNum += tmpAnswer[i-1]
        if passedNum != 0:
            tmpAnswer[i-1] = (i, tmpAnswer[i-1]/passedNum)
        else:
            tmpAnswer[i-1] = (i, 0)

    answer = sorted(tmpAnswer[:-1], key=lambda x: x[1], reverse=True)
    answer = list(map(lambda x: x[0], answer))
    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
