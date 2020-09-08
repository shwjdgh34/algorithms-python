from bisect import bisect_left, bisect_right


array = [[] for _ in range(10001)]
reversed_array = [[] for _ in range(10001)]


def countByRange(arr, left_value, right_value):
    left_index = bisect_left(arr, left_value)
    right_index = bisect_right(arr, right_value)
    return right_index - left_index


def solution(words, queries):
    answer = []

    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])  # 단어 뒤집어서 넣기

    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()

    for q in queries:
        if q[0] == '?':  # 접두사에 와일드카드
            res = countByRange(
                reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        else:
            res = countByRange(array[len(q)], q.replace(
                '?', 'a'), q.replace('?', 'z'))

        answer.append(res)

    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
               ["fro??", "fr???", "fro???", "pro?"]))
