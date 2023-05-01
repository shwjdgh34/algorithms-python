class Solution(object):
    def climbStairs(self, n):
        memo = {}

        def dp(n):
            if n == 1:
                return 1
            if n == 2:
                return 0
            if n not in memo:
                memo[n] = dp(n - 1) + dp(n - 2)
            return memo[n]
        return dp(n)

# class Solution(object):
#     def climbStairs(self, n):
#         dp = [-1] * (n + 1)

#         dp[0] = 1
#         dp[1] = 1

#         for i in range(2, n + 1):
#             dp[i] = dp[i-1] + dp[i-2]

#         return dp[n]


# s = Solution()
# print(s.climbStairs(3))


def climbStairs(n):
    dp = [-1] * (n + 1)

    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]


print(climbStairs(3))
