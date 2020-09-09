def solution(n, weak, dist):
    answer = 0
    distL = len(dist)
    dist.reverse()

    def dfs(weak, dist):
        minNum = 987654321
        if len(weak) == 0:
            return distL - len(dist)
        if len(dist) == 0:
            return minNum

        for w in weak:
            copyWeak = weak[:]
            for d in range(dist[0]+1):
                weakPosition = (w + d) % 12
                if weakPosition in copyWeak:
                    copyWeak.remove(weakPosition)

            ret = dfs(copyWeak, dist[1:])
            if minNum > ret:
                minNum = ret
        return minNum

    answer = dfs(weak, dist)
    if answer == 987654321:
        answer = -1
    return answer


print(solution(12,	[1, 5, 6, 10],	[1, 2, 3, 4]))
