# nums = {4, 1, 9, 7, 5, 3, 16 }
# target = 14
def twosum(nums, target):
    nums.sort()
    l, r = 0, len(nums)-1

    while l < r :
        if nums[l] + nums[r] > target:
            r -= 1
        elif nums[l] + nums[r] < target:
            l += 1
        elif nums[l] + nums[r] == target:
            return True
    return False

print(twosum(nums = [4, 1, 9, 7, 5, 3, 16] , target = 14))