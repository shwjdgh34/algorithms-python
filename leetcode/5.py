class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        longest_palindrome_start, longest_palindrome_len = 0, 1

        for end in range(0, n):
            for start in range(end - 1, -1, -1):
                # print('start: %s, end: %s' % (start, end))
                if s[start] == s[end]:
                    if end - start == 1 or dp[start + 1][end - 1]:
                        dp[start][end] = True
                        palindrome_len = end - start + 1
                        if longest_palindrome_len < palindrome_len:
                            longest_palindrome_start = start
                            longest_palindrome_len = palindrome_len
        return s[longest_palindrome_start: longest_palindrome_start + longest_palindrome_len]


'''
class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        max_palindrome = ""
        for i in range(n):

            def two_pointer(s, left, right):
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    left -= 1
                    right += 1
                return s[left+1:right]

            rString1 = two_pointer(s, i, i)
            rString2 = two_pointer(s, i, i+1)

            if len(max_palindrome) < len(rString1):
                max_palindrome = rString1
            if len(max_palindrome) < len(rString2):
                max_palindrome = rString2

        return max_palindrome
'''    

s = Solution()
print(s.longestPalindrome("babad"))