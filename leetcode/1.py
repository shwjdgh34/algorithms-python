'''
완전탐색 O(n^2)
'''
# def twoSum(nums, target):
#     n = len(nums)
#     for i in range(n):
#         for j in range(i+1, n):
#             if nums[i] + nums[j] == target:
#                 return [i, j]

# twoSum(nums = [4,1,9,7,5,3,16], target = 14)


# def twoSum(nums, target):
#     # O(nlogn)
#     nums.sort()
#     l, r = 0, len(nums)-1

#     # O(n)
#     while l < r:
#             if target > nums[l] + nums[r] : l += 1
#             elif target < nums[l] + nums[r] : r -= 1
#             else: return [l, r]

#     return False
'''
정렬 이용 O(nlogn)
'''


def twoSum(self, nums, target):

    origin_indices = {}

    for idx, val in enumerate(nums):
        if val in origin_indices:
            origin_indices[val].append(idx)
        else:
            origin_indices[val] = [idx]

    nums.sort()

    l, r = 0, len(nums)-1

    while l < r:
        if target > (nums[l] + nums[r]):
            l += 1
        elif target < (nums[l] + nums[r]):
            r -= 1
        else:
            return [origin_indices[nums[l]][0], origin_indices[nums[r]][-1]]


class Solution(object):
    def twoSum(self, nums, target):
        nums = [[n, i] for i, n in enumerate(nums)]
        nums.sort(key=lambda x: x[0])
        l, r = 0, len(nums) - 1

        while l <= r:
            num_sum = nums[l][0] + nums[r][0]
            if num_sum == target:
                return [nums[l][1], nums[r][1]]
            elif num_sum > target:
                r -= 1
            else:
                l += 1


def twoSum(nums, target):
    seen = {}
    for i, v in enumerate(nums):
        another = target - v

        if another in seen:
            return [seen[another], i]
        else:
            seen[v] = i

    return [-1, -1]
