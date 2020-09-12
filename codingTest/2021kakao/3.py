def solution(info, query):
    column = [['java', 'cpp', 'python'], ['backend', 'frontend'],
              ['junior', 'senior'], ['chicken', 'pizza']]
    database = {'java': {'backend': {'junior': {'chicken': [], 'pizza': []},
                                     'senior': {'chicken': [], 'pizza': []}},
                         'frontend': {'junior': {'chicken': [], 'pizza': []},
                                      'senior': {'chicken': [], 'pizza': []}}},

                'cpp': {'backend': {'junior': {'chicken': [], 'pizza': []},
                                    'senior': {'chicken': [], 'pizza': []}},
                        'frontend': {'junior': {'chicken': [], 'pizza': []},
                                     'senior': {'chicken': [], 'pizza': []}}},


                'python': {'backend': {'junior': {'chicken': [], 'pizza': []},
                                       'senior': {'chicken': [], 'pizza': []}},
                           'frontend': {'junior': {'chicken': [], 'pizza': []},
                                        'senior': {'chicken': [], 'pizza': []}}}}
    answer = []

    def search(qArr, i, db):
        global count
        if i == 4:
            for score in db:
                if score >= qArr[i]:
                    count += 1
            return

        for v in column[i]:
            if qArr[i] == v or qArr[i] == '-':
                search(qArr, i+1, db[v])

    for data in info:
        dataArr = data.split()
        database[dataArr[0]][dataArr[1]][dataArr[2]
                                         ][dataArr[3]].append(int(dataArr[4]))
    global count
    for q in query:
        qArr = q.replace(' and ', ' ').split()
        qArr[4] = int(qArr[4])
        count = 0
        search(qArr, 0, database)
        answer.append(count)

    return answer


print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], [
      "java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))
