class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, v in enumerate(nums):
            another = target - v

            if another in seen:
                return [seen[another], i]
            else:
                seen[v] = i

        return [-1, -1]


'''
완전탐색 O(n^2)
'''

# class Solution(object):
#     def twoSum(self, nums, target):
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j];
