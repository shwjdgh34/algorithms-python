# # https://leetcode.com/problems/house-robber/

# #Top-down memoization
# # 함수안의 함수가 있는경우, 바깥 함수에서 정의한 변수도 쓸 수 있다.
# # memoization을 위해 hashmap을 사용

# class Solution(object):
#     def rob(self, nums):
#         memo = {}
        
#         def dp(i):
#             if i == 0: return nums[0] 
#             if i == 1: return max(nums[0], nums[1])
            
#             if i not in memo:
#                 memo[i] = max(dp(i-1), dp(i-2)+nums[i])

#             return memo[i]
        
#         return dp(len(nums) - 1)

# # Bottom-up tabulation

# class Solution(object):
#     def rob(self, nums):
#         dp = [-1 for i in range(len(nums))]
        
#         dp[0] = nums[0]
        
#         if len(nums) > 1:
#             dp[1] = max(nums[0], nums[1])

#             for i in range(2,len(nums)):
#                dp[i] = max(dp[i-2]+nums[i], dp[i-1])

#         return dp[len(nums)-1]
            



# s = Solution()
# print(s.rob([2,7,9,3,1]))


class Solution:
    def rob(self, nums):        
        dp = {}
        
        def dfs(cur_i, nums, dp, prev_robbed):
            if cur_i >= len(nums):
                return 0
            
            if (cur_i, prev_robbed) in dp:
                return dp[(cur_i, prev_robbed)]
            
            dp[(cur_i, prev_robbed)] = dfs(cur_i+1, nums, dp, False)
            if not prev_robbed:
                dp[(cur_i, prev_robbed)] = max(dp[(cur_i, prev_robbed)], dfs(cur_i+1, nums, dp, True) + nums[cur_i])
                
            return dp[(cur_i, prev_robbed)]
        
        dfs(0, nums, dp, False)
        
        return max(dp.values())


s= Solution()
s.rob([2,7,9,3,1])