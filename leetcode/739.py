# # O(n^2)
# def dailyTemperatures(temperatures):
#     n = len(temperatures)
#     answer = [0] * n
#     for cur_day in range(n):
#         for future_day in range(cur_day + 1, n):
#             if temperatures[future_day] > temperatures[cur_day]:
#                 answer[cur_day] = future_day - cur_day
#                 break
#     return answer

# # O(n)

# def dailyTemperatures(temperatures):
#     ans = [0] * len(temperatures)
#     stack = []
#     for cur_day, cur_temp in enumerate(temperatures):
#         while stack and stack[-1][1] < cur_temp:
#             prev_day, _ = stack.pop()
#             ans[prev_day] = cur_day - prev_day
#         stack.append((cur_day, cur_temp))
#     return ans


def dailyTemperatures(temperatures):
    stack = []
    ans = [0 for i in range(len(temperatures))]
    i = 0
    while i < len(temperatures):
        if not stack:
            stack.append((temperatures[i],i)) #튜플로 온도정보와 index정보 저장
        else:
            while stack and stack[-1][0] < temperatures[i] :
                index = stack[-1][1]
                ans[index] = i - index
                stack.pop()
            stack.append((temperatures[i],i))
        i+=1
    return ans

print(dailyTemperatures([73,74,75,71,69,72,76,73]))

