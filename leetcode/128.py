# Hash set 참고 자료  https://stackoverflow.com/questions/3949310/how-is-set-implemented
# 문제 이해하기에서 1,1,2,2,3,4,5는 어떻게 처리하는가?

# O(nlogn) => sort
# [], [2] ㅇ이거 인풋으로 했을 때  생기는 오류를 잡아야 한다
def longestConsecutive(nums):
    n = len(nums)
    nums.sort()
    count = 1
    longest = 1 if nums else 0  # 이걸 수정했음 [], [2]일때를 대비해서
    # sorted_num = sorted(nums)

    for i in range(1, n):

        if nums[i] == nums[i-1]:  # [1,1,2,2,3,4,5] 이 코드 때문에 넣었다.
            continue
        if nums[i] == nums[i-1] + 1:
            count += 1
        else:
            count = 1
        # 이게 너무 불필요하게 반복된다고 느낀다면 else:에 넣고, return에 max(longest, count)를 해도 된다.
        longest = max(longest, count)
    return longest

# O(^3) => Brute force

# def longestConsecutive(nums):
#     longest_streak = 0

#     for num in nums:
#         current_num = num
#         current_streak = 1

#         while current_num + 1 in nums: # 여기거 O(n)이 걸린다. dictionary의 in과 다르다. => 이걸 dictionary로 쓰면 시간복잡도를 O(n^2)으로 할 수 있다.
#             current_num += 1
#             current_streak += 1

#         longest_streak = max(longest_streak, current_streak)

#     return longest_streak


# O(n):
# 시작점을 먼저 찾는다.
# 그리고 while문으로 쭈르르륵 연속된 수 센다. (hashtable, hashset 덕분에 이지하다)
# for문 안에 있는 while문인데, 시간복잡도가 어떻게 되나요??! => 나중에 시간복잡도 설명할 때 이 내용 추가하면 좋을 것 같다.
def longestConsecutive(nums):
    longest = 0
    num_dict = {num: True for num in nums}  # comprehension
    # num_set = set(nums)

    # for num in nums:
    #     num_dict[num] = 1

    # num_set = set(nums)
    for num in num_dict:
        if num - 1 not in num_dict:
            cnt = 1
            target = num + 1
            while target in num_dict:  # 성난오리님 코드 설명
                target += 1
                cnt += 1
            longest = max(longest, cnt)

    return longest


print(longestConsecutive([1, 1, 2, 2, 3, 4, 5]))
