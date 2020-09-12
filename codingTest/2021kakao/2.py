def solution(orders, course):
    answer = []
    tmpAnswer = []
    # hashmap = {}
    global picked
    picked = ''
    maxArr = [0 for _ in range(11)]
    # def visited(picked):
    #     if picked in hashmap:
    #         return True
    #     else:
    #         False

    def search(picked):
        count = 0
        for order in orders:
            sPicked = set(picked)
            sOrder = set(order)
            if sPicked & sOrder == sPicked:
                count += 1
        if count >= 2:
            if maxArr[len(picked)] < count:
                maxArr[len(picked)] = count
            tmpAnswer.append((picked[:], count))

    def bf(order, n, start):
        global picked
        if len(picked) in course:
            search(picked)
        for i in range(start, n):
            picked = picked + (order[i])
            bf(order, n, i+1)
            picked = picked[:-1]

    for i, order in enumerate(orders):
        orders[i] = ''.join(sorted(order))
    for order in orders:
        bf(order, len(order), 0)

    for picked, num in tmpAnswer:
        if maxArr[len(picked)] == num:
            answer.append(picked)

    answer = sorted(list(set(answer)))

    return answer


print(solution(["BACFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
