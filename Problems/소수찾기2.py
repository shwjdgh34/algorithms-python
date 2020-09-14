'''
완전탐색 이용
'''
import math


def isPrime(num):
    sqrtNum = int(math.sqrt(num))
    for i in range(2, sqrtNum + 1):
        if num % i == 0:
            return False

    return num > 1


def solution(numbers):
    numsArr = list(numbers)
    n = len(numsArr)
    answer = []
    selected = [False]*n

    def bf(selected, curNumber=''):
        if curNumber != '' and isPrime(int(curNumber)):
            answer.append(int(curNumber))

        for i in range(0, n):
            if selected[i]:
                continue
            selected[i] = True
            bf(selected, curNumber+numbers[i])
            selected[i] = False

    bf(selected, '')
    answer = list(set(answer))
    print(answer)
    return len(answer)


print(solution('17'))
