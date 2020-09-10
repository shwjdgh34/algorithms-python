def solution(record):
    answer = []
    database = {}
    for r in record:
        rArr = r.split(' ')
        action, uid = rArr[0], rArr[1]

        if len(rArr) == 3:
            database[uid] = rArr[2]
        if action != 'Change':
            answer.append([action, uid])

    for i, ans in enumerate(answer):
        ansStr = ''
        if ans[0] == 'Enter':
            ansStr = database[ans[1]] + '님이 들어왔습니다.'
        else:
            ansStr = database[ans[1]] + '님이 나갔습니다.'
        answer[i] = ansStr

    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo",
                "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
