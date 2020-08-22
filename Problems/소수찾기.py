'''
에라토스테네스의 체를 이용하여 훨씬 빠른 속도로 풀이할 수 있다.
'''


def solution(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    if m < 2:
        prime_list = [2]
    else:
        for i in range(2, m + 1):
            if sieve[i] == True:           # i가 소수인 경우
                for j in range(i+i, n, i):  # i이후 i의 배수들을 False 판정
                    sieve[j] = False
        prime_list = [i for i in range(2, n) if sieve[i] == True]
    # 소수 목록 산출

    return len(prime_list)


'''
에라토스테네스의 체를 집합으로 표현하여 풀이한 것이다.
'''


def solution(n):
    num = set(range(2, n+1))

    for i in range(2, n+1):
        if i in num:
            num -= set(range(2*i, n+1, i))
    return len(num)


'''
에라토스테네스의 체를 사용하지 않는다면 보통 이런 방식으로 풀 것이다.
'''


def isPrime(n):
    if n == 1:
        return False
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True


def solution(n):
    count = 0
    for x in range(1, n+1):
        if isPrime(x):
            count += 1
    return count
