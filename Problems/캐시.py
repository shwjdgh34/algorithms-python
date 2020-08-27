'''
deque의 argument로 maxlen 쓴 풀이
'''

from collections import deque


def solution(cacheSize, cities):
    answer = 0
    lowerCaseCities = [x.lower() for x in cities]
    cache = deque(maxlen=cacheSize)
    for city in lowerCaseCities:
        # hit!
        if city in cache:
            answer += 1
            cache.remove(city)

        # falut!
        else:
            answer += 5

        cache.append(city)

    return answer


'''
maxlen 안쓴 풀이
'''

'''
def solution(cacheSize, cities):
    answer = 0
    lowerCaseCities = [x.lower() for x in cities]
    cache = deque([])
    for city in lowerCaseCities:
        # hit!
        if city in cache:
            answer += 1
            cache.remove(city)

        # falut!
        else:
            answer += 5
            if cache and len(cache) == cacheSize:
                cache.popleft()

        if len(cache) < cacheSize:
            cache.append(city)

    return answer
'''
print(solution(3, ['Jeju', 'Pangyo', 'Seoul', 'NewYork',
                   'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']))
