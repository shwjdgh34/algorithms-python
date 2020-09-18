import bisect


def solution(food_times, k):
    remainedFoodNum = len(food_times)

    def count(n):
        l = bisect.bisect_left(sortedTimes, n)
        r = bisect.bisect_right(sortedTimes, n)
        return r-l
    sortedTimes = sorted(food_times)

    sortedTimesSet = set(sortedTimes)
    sortedTimesInfo = []
    for t in sortedTimesSet:
        sortedTimesInfo.append((t, count(t)))

    prevMin = 0

    for nextMin, nextMinNum in sortedTimesInfo:
        times = nextMin-prevMin
        if k - remainedFoodNum * times >= 0:
            k -= remainedFoodNum * times
            remainedFoodNum -= nextMinNum
            prevMin = nextMin
        else:
            k %= remainedFoodNum
            break

    for i, time in enumerate(food_times):
        if prevMin < time:
            if k == 0:
                return i+1
            k -= 1

    return -1

print(solution([4, 2, 3, 6, 7, 1, 5, 8],	15))