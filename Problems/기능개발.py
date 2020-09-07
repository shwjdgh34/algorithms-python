'''
Stack
O(n)
'''
import math


def solution(progresses, speeds):

    n = len(progresses)
    answer = []
    terms = []
    for i in range(n):
        cur = math.ceil((100 - progresses[i]) / speeds[i])
        if len(terms) == 0:
            terms.append(cur)
        elif terms[0] >= cur:
            terms.append(cur)
        elif terms[0] < cur:
            count = 0
            while terms:
                terms.pop()
                count += 1
            answer.append(count)
            terms.append(cur)

        if i == n-1:
            count = 0
            while terms:
                terms.pop()
                count += 1
            answer.append(count)

    return answer


print(solution([93, 30, 55], [1, 30, 5]))


'''
Brute force 
O(n)
'''

'''
def solution(progresses, speeds):

    n = len(progresses)
    answer = []
    terms = []
    for i in range(n):
        if(terms and )
        terms[i] = math.ceil((100 - progresses[i]) / speeds[i])

    i = 0
    while i < n:
        count = 1
        while i + count < n and terms[i] >= terms[i + count]:
            count += 1
        i += count
        answer.append(count)

    return answer


print(solution(	[93, 30, 55], [1, 30, 5]))
'''
