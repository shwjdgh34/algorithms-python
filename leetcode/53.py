# O(n)
# DP: tabulation

# class Solution(object):
#     def maxSubArray(self, nums):
#         max_array = [0 for i in range(len(nums))]
#         max_array[0] = nums[0]

#         for i, num in enumerate(nums[1:], 1):
#             if max_array[i-1] > 0:
#                 max_array[i] = num + max_array[i-1]
#             else :
#                 max_array[i] = num

#         return max(max_array)

class Solution(object):
    def maxSubArray(self, nums):
        max_array = [0 for i in range(len(nums))]
        max_array[0] = nums[0]

        for i, num in enumerate(nums[1:], 1):
            max_array[i] = max(num, num + max_array[i-1])

        return max(max_array)

s = Solution()
print(s.maxSubArray([5,4,-1,7,8]))





        
            
        