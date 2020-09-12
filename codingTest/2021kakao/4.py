import heapq


def solution(n, s, a, b, fares):
    answer = 0
    mygraph = {}

    for i in range(1, n+1):
        mygraph[i] = {}

    # 방향 그래프
    for fare in fares:
        c, d, f = fare[0], fare[1], fare[2]
        if c in mygraph and d in mygraph[c]:
            if f < mygraph[c][d]:
                mygraph[c][d] = f
                mygraph[d][c] = f

        else:
            mygraph[c][d] = f
            mygraph[d][c] = f

    def dijkstra(graph, start, end):
        distances = {vertex: [100000000000, start] for vertex in graph}
        distances[start] = [0, start]
        queue = []
        heapq.heappush(queue, [distances[start][0], start])

        while queue:
            current_distance, current_vertex = heapq.heappop(queue)
            if distances[current_vertex][0] < current_distance:
                continue

            for adjacent, weight in graph[current_vertex].items():
                distance = current_distance + weight

                if distance < distances[adjacent][0]:

                    distances[adjacent] = [distance, current_vertex]
                    heapq.heappush(queue, [distance, adjacent])
        answer = 0
        path = end
        if distances[path][1] == start:
            answer += distances[path][0]
        while distances[path][1] != start:
            answer += distances[path][0]
            path = distances[path][1]

        # print(answer)
        return answer
    min_ = 100000000000
    for i in range(1, n+1):
        together = dijkstra(mygraph, s, i)
        toA = dijkstra(mygraph, i, a)
        toB = dijkstra(mygraph, i, b)
        total = together + toA + toB
        if min_ > total:
            min_ = total
    answer = min_

    return answer


print(solution(6,	4,	5,	6,	[[2, 6, 6], [6, 3, 7], [4, 6, 7], [
      6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]))
