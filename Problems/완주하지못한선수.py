'''
O(nlogn): sort()
'''

#
# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
#
#     for i in range(len(completion)):
#         if participant[i] != completion[i]:
#             return participant[i]
#
#     return participant[-1]
#

'''
O(n): hashmap
'''

# def solution(participant, completion):
#     hashmap = {}
#     for v in completion:
#         if v in hashmap:
#             hashmap[v] += 1
#         else:
#             hashmap[v] = 1
#
#     for v in participant:
#         if not (v in hashmap) or hashmap[v] == 0:
#             return v
#         else:
#             hashmap[v] -= 1

'''
O(n): collections Counter
'''
# from collections import Counter
#
#
# def solution(participant, completion):
#     answer = Counter(participant) - Counter(completion)
#     return list(answer.keys())[0]


print(solution(["marina", "josip", "nikola", "vinko", 'filipa'], ['josip', 'filipa', 'marina', 'nikola']))
