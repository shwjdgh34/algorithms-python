# Runtime: 16 ms, faster than 75.57% of Python online submissions for N-th Tribonacci Number.
# Memory Usage: 13.3 MB, less than 65.95% of Python online submissions for N-th Tribonacci Number.
# top-down
class Solution(object):
    def tribonacci(self, n):

        memo = {}
        def dp(i):
            if i == 0 : return 0
            if i == 1 : return 1
            if i == 2 : return 1


            if i not in memo:
                memo[i] = dp(i-1) + dp(i-2) + dp(i-3)

            return memo[i]

        return dp(n)


# Runtime: 24 ms, faster than 16.24% of Python online submissions for N-th Tribonacci Number.
# Memory Usage: 13.3 MB, less than 65.95% of Python online submissions for N-th Tribonacci Number.
# bottom-up

class Solution(object):
    def tribonacci(self, n):

        if n == 0 : return 0
        if n == 1 : return 1
        if n == 2 : return 1
        t = [0] * (n+1)
        
        t[0] = 0
        t[1] = 1
        t[2] = 1

        for i in range(3, n+1):
            t[i] = t[i-1]+t[i-2]+t[i-3]

        return t[n]


s = Solution()
print(s.tribonacci(25))