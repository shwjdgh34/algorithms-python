# 접근 방법
# stack을 이용하면 될 것 같다.

class Solution(object):
    def romanToInt(self, s):
        r2i = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        stack = []

        for roman in s:
            num = r2i[roman]
            if stack and stack[-1] < num:
                num = num - stack.pop()
            stack.append(num)

        total = 0
        while stack:
            total = total + stack.pop()
        
        return total


s = Solution()
print(s.romanToInt("MCMXCIV"))


