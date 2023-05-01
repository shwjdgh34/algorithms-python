# # O(2^m)
# class Solution(object):
#     def maximumScore(self, nums, multipliers):
#         m = len(multipliers)

#         def dfs(nums, i, sum):
#             if i >= m :
#                 return sum
            
#             return max(dfs(nums[1:], i+1, sum+nums[0]* multipliers[i]),
#             dfs(nums[0:-1], i+1, sum+nums[-1]* multipliers[i]))

#         return dfs(nums, 0, 0)







from typing import List
from functools import lru_cache

# class Solution:
#     def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
#         # lru_cache from functools automatically memoizes the function
        
#         #@lru_cache(2000)
        
        
#         def dp(i, left):
#             # Base case
#             if i == m:
#                 return 0

#             mult = multipliers[i]
#             right = n - 1 - (i - left)

#             if memo[i][left] == 'inf':
#                 ret1[i][left] = mult * nums[left] + dp(i + 1, left + 1)
#                 ret2[i][left] = mult * nums[right] + dp(i + 1, left)

#             # Recurrence relation
            
#                 memo[i][left] = max(ret1[i][left], ret2[i][left])
#             return memo[i][left]
                       
#         n, m = len(nums), len(multipliers)
#         memo = [['inf' for i in range(m)] for j in range(m)] 
#         ret1 = [['inf' for i in range(m)] for j in range(m)] 
#         ret2 = [['inf' for i in range(m)] for j in range(m)] 

#         return dp(0, 0)



class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
                
        dp = {} # l, r
        
        i = 0
        a = 10
        def incre():
            print(a)

        incre()
        print(a)
        # multipliers[i]
        def dfs(nums, l, r, i):
            
            multipliers[0] = 0
            if i == len(multipliers):
                return 0
            
            if (l,r) in dp:
                return dp[(l,r)]

            dp[(l,r)] = max(dfs(nums, l+1, r, i+1) + nums[l] * multipliers[i],
                           dfs(nums, l, r-1, i+1) + nums[r] * multipliers[i])
            
            return dp[(l,r)]
        
        return dfs(nums, 0, len(nums)-1, 0)





s = Solution()
print(s.maximumScore([-5,-3,-3,-2,7,1], [-10,-5,3,4,6]))