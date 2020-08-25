from collections import deque


def solution(priorities, location):
    answer = []

    dq = deque([(l, v) for l, v in enumerate(priorities)])

    while(True):
        cur = dq.popleft()
        if any(cur[1] < dqData[1] for dqData in dq):
            dq.append(cur)
        elif(cur[0] == location):
            answer.append(cur)
            return len(answer)
        else:
            answer.append(cur)


print(solution([1, 1, 9, 1, 1, 1], 0))
