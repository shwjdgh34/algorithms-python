class Solution(object):
    def searchInsert(self, nums, target):
        if len(nums) == 0:
            return 0

        left, right = 0, len(nums)
        mid = 0
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid
            else:
                right = mid + 1
        return mid


s = Solution()
print(s.searchInsert(nums = [1,3,5,6], target = 5))