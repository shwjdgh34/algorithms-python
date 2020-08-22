'''
Stack을 이용한 나의 풀이 O(n)
'''


def solution(prices):
    answer = [0]*len(prices)
    stack = []

    for i, price in enumerate(prices):
        while stack and price < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j

    return answer


print(solution([1, 2, 3, 2, 3]))


'''
완전탐색 O(n^2)
'''


# def solution(prices):
#     answer = [0] * len(prices)
#     for i in range(len(prices)):
#         for j in range(i+1, len(prices)):
#             if prices[i] <= prices[j]:
#                 answer[i] += 1
#             else:
#                 answer[i] += 1
#                 break
#     return answer
