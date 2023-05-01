# Runtime: 52 ms, faster than 31.45% of Python online submissions for Min Cost Climbing Stairs.
# Memory Usage: 15.9 MB, less than 8.21% of Python online submissions for Min Cost Climbing Stairs.
# Top-down

"""
class Solution(object):
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        memo = {}
        # dp(i)의 반환값이 무엇을 의미할 것이냐를 잘 정의해야 한다.
        def dp(i):
            if i == 0 or i == 1:
                return 0
            
            if i not in memo:
                # memo[i] = min(dp(i-1), dp(i-2)) + cost[i]로 했는데, 
                # 이러면 i가 dp()에 대한 state가 되지 못해서, 아래 코드로 변경함
                # 변경한 코드는 dp(i)의 반환값이 i에 도달 할 수 있는 최소 cost를 의미 하게 됨
                memo[i] = min(dp(i-1) + cost[i-1], dp(i-2) + cost[i-2]) 

            return memo[i]

        return dp(n)

"""


# Runtime: 32 ms, faster than 99.03% of Python online submissions for Min Cost Climbing Stairs.
# Memory Usage: 13.9 MB, less than 20.32% of Python online submissions for Min Cost Climbing Stairs.
# bottom-up


class Solution(object):
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        dp = [0 for i in range(n+1)]

        dp[0] = 0
        dp[1] = 0
        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

        return dp[n]


s = Solution()
print(s.minCostClimbingStairs([10, 15, 20]))


#  --------------------------------------------------------------------------------------------------------------------


# class Solution(object):
#     def minCostClimbingStairs(self, cost):
#         n = len(cost)

#         def dfs(n):
#             if n == 0:
#                 return 0
#             if n == 1:
#                 return 0
#             return min(dfs(n-1) + cost[n-1], dfs(n-2) + cost[n-2])
#         return dfs(n)


class Solution(object):
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        memo = {}

        def dp(n):
            if n == 0:
                return 0
            if n == 1:
                return 0

            if n not in memo:
                memo[n] = min(dp(n-1) + cost[n-1], dp(n-2) + cost[n-2])
            return memo[n]
        return dp(n)


"""
class Solution(object):
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        
        memo = {}
        def dfs(n):
            if n == 0: return 0
            if n == 1: return 0
            memo[n] = min(dfs(n-1) + cost[n-1], dfs(n-2) + cost[n-2])
            return memo[n]

"""

s = Solution()
# print(s.minCostClimbingStairs([10,15,20]))
print(s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
