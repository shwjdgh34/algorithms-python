'''
1. 왼쪽에서 작은거 1  나(젤 작으면 통과)  오른쪽에서 작은거 1
1. 왼쪽에서 작은거 1  나(두번쨰도 통과)  오른쪽에서 작은거 1

    결론: 중간에 있는애가 제일 크면 안된다

'''


def solution(a):
    n = len(a)
    answer = 1 if n == 1 else 2

    l2r = [0] * n
    r2l = [0] * n

    # 이걸 987654321로 해서 틀렸다
    min_ = 1000000001
    for i, val in enumerate(a):
        if min_ > val:
            min_ = val
        l2r[i] = min_

    min_ = 1000000001
    for i, val in enumerate(a[::-1]):
        if min_ > val:
            min_ = val
        r2l[n-1-i] = min_

    for i in range(1, n-1):
        if a[i] <= max(l2r[i-1], r2l[i+1]):
            answer += 1

    return answer


print(solution([-1000000000, -999999998, -999999997, -999999996, -999999999]))
