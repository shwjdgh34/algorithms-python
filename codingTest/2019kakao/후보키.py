def solution(relation):
    column = len(relation[0])
    row = len(relation)
    candidateKey = []
    for case in range(1, 2**column):
        minimality = True
        uniqueness = True
        hashmap = {}
        for key in candidateKey:
            if key & case == key:
                minimality = False
                break
        if minimality == False:
            continue
        for r in range(row):
            tmpStr = ''
            curCols = []
            for k in range(column):
                if case & (1 << k):
                    curCols.append(k)
            for c in curCols:
                tmpStr += relation[r][c]
            if tmpStr in hashmap:
                uniqueness = False
                break
            hashmap[tmpStr] = True
        if uniqueness:
            candidateKey.append(case)

    answer = len(candidateKey)
    return answer


print(solution([
    ["100", "ryan", "music", "2"],
    ["200", "apeach", "math", "2"],
    ["300", "tube", "computer", "3"],
    ["400", "con", "computer", "4"],
    ["500", "muzi", "music", "3"],
    ["600", "apeach", "music", "2"]]))
