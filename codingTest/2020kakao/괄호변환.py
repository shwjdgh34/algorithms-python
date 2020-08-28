def isCorrectStr(u):
    stack = []
    for c in u:
        if stack and stack[-1] == '(' and c == ')':
            stack.pop()
        else:
            stack.append(c)
    if stack:
        return False
    else:
        return True


def solution(p):
    answer = ''
    if not p:
        return p

    countL = 0
    countR = 0

    u = ''
    v = ''

    for i, c in enumerate(p):
        if c == '(':
            countL += 1
        else:
            countR += 1
        if countL == countR:
            u = p[:i+1]
            v = p[i+1:]
            break

    if isCorrectStr(u):
        return u+solution(v)
    else:
        newU = ''
        for c in u[1:-1]:
            if c == '(':
                newU += ')'
            else:
                newU += '('

        answer = '(' + solution(v) + ')' + newU
    return answer


print(solution("()))((()"))
