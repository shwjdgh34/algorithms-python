# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    stack = []
    for c in S:
        if stack and CanErase(stack[-1], c):
            stack.pop()
        else:
            stack.append(c)

    answer = ''.join(stack)
    return answer


def CanErase(c1, c2):
    if {c1, c2} == {'A', 'B'} or {c1, c2} == {'C', 'D'}:
        return True
    return False


print(solution("CABABD"))
